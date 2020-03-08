const express = require("express");
const cors = require("cors");
const app = express();
const uuidv4 = require("uuid/v4");
const md5 = require("md5");
const jwt = require("express-jwt");
const jsonwebtoken = require("jsonwebtoken");
const server = require("http").createServer(app);
const io = require("socket.io")(server);
const bigInt = require("big-integer");
const { flag, p, n, _clearPIN, jwtSecret } = require("./flag");

const config = {
  port: process.env.PORT || 8081,
  width: 120,
  height: 80,
  usersOnline: 0,
  message: "Hello there!",
  p: p,
  n: n,
  adminUsername: "hacktm",
  whitelist: ["/", "/login", "/init"],
  backgroundColor: 0x888888,
  version: Number.MIN_VALUE
};

io.sockets.on("connection", function (socket) {
  config.usersOnline++;
  socket.on("disconnect", function () {
    config.usersOnline--;
  });
});

let users = {
  0: {
    username: config.adminUsername,
    rights: Object.keys(config)
  }
};

let board = new Array(config.height)
  .fill(0)
  .map(() => new Array(config.width).fill(config.backgroundColor));
let boardString = boardToStrings();

app.use(express.json());
app.use(cors());
app.use(
  jwt({ secret: jwtSecret }).unless({
    path: config.whitelist
  })
);
app.use(function (error, req, res, next) {
  if (error.name === "UnauthorizedError") {
    res.json(err("Invalid token or not logged in."));
  }
});

function sign(o) {
  return jsonwebtoken.sign(o, jwtSecret);
}

function isAdmin(u) {
  return u.username.toLowerCase() == config.adminUsername.toLowerCase();
}

function ok(data = {}) {
  return { status: "ok", data: data };
}

function err(msg = "Something went wrong.") {
  return { status: "error", message: msg };
}

function onlyUnique(value, index, self) {
  return self.indexOf(value) === index;
}

app.get("/", (req, res) => {
  // Get current board
  res.json(ok({ board: boardString }));
});

app.post("/init", (req, res) => {
  // Initialize new round and sign admin token
  // RSA protected!
  // POST
  // {
  //   p:"0",
  //   q:"0"
  // }

  let { p = "0", q = "0", clearPIN } = req.body;

  let target = md5(config.n.toString());

  let pwHash = md5(
    bigInt(String(p))
      .multiply(String(q))
      .toString()
  );

  if (pwHash == target && clearPIN === _clearPIN) {
    // Clear the board
    board = new Array(config.height)
      .fill(0)
      .map(() => new Array(config.width).fill(config.backgroundColor));
    boardString = boardToStrings();

    io.emit("board", { board: boardString });
  }

  //Sign the admin ID
  let adminId = pwHash
    .split("")
    .map((c, i) => c.charCodeAt(0) ^ target.charCodeAt(i))
    .reduce((a, b) => a + b);

  console.log(adminId);

  res.json(ok({ token: sign({ id: adminId }) }));
});

app.get("/flag", (req, res) => {
  // Get the flag
  // Only for root
  if (req.user.id == 0) {
    res.send(ok({ flag: flag }));
  } else {
    res.send(err("Unauthorized"));
  }
});

app.get("/serverInfo", (req, res) => {
  // Get server info
  // Only for logged in users

  let user = users[req.user.id] || { rights: [] };
  let info = user.rights.map(i => ({ name: i, value: config[i] }));
  res.json(ok({ info: info }));
});

app.post("/paint", (req, res) => {
  // Paint on the canvas
  // Only for logged in users
  // POST
  // {
  //   x:0,
  //   y:0
  // }
  let user = users[req.user.id] || {};

  x = req.body.x;
  y = req.body.y;

  let color = user.color || 0x0;

  if (board[y] && board[y][x] >= 0) {
    board[y][x] = color;
    boardString = boardToStrings();
    io.emit("change", { change: { pos: [x, y], color: color } });
    res.send(ok());
  } else {
    res.send(err("Invalid painting"));
  }
});

app.post("/updateUser", (req, res) => {
  // Update user color and rights
  // Only for admin
  // POST
  // {
  //   color: 0xDEDBEE,
  //   rights: ["height", "width", "usersOnline"]
  // }
  let uid = req.user.id;
  let user = users[uid];
  if (!user || !isAdmin(user)) {
    res.json(err("You're not an admin!"));
    return;
  }
  let color = parseInt(req.body.color);
  users[uid].color = (color || 0x0) & 0xffffff;
  let rights = req.body.rights || [];
  if (rights.length > 0 && checkRights(rights)) {
    users[uid].rights = user.rights.concat(rights).filter(onlyUnique);
  }

  res.json(ok({ user: users[uid] }));
});

app.post("/login", (req, res) => {
  // Login
  // POST
  // {
  //   username: "dumbo",
  // }

  let u = {
    username: req.body.username,
    id: uuidv4(),
    color: Math.random() < 0.5 ? 0xffffff : 0x0,
    rights: [
      "message",
      "height",
      "width",
      "version",
      "usersOnline",
      "adminUsername",
      "backgroundColor"
    ]
  };

  if (isValidUser(u)) {
    users[u.id] = u;
    res.send(ok({ token: sign({ id: u.id }) }));
  } else {
    res.json(err("Invalid creds"));
  }
});

function isValidUser(u) {
  return (
    u.username.length >= 3 &&
    u.username.toUpperCase() !== config.adminUsername.toUpperCase()
  );
}

function boardToStrings() {
  return board.map(b => b.join(","));
}

function checkRights(arr) {
  let blacklist = ["p", "n", "port"];
  for (let i = 0; i < arr.length; i++) {
    const element = arr[i];
    if (blacklist.includes(element)) {
      return false;
    }
  }
  return true;
}

server.listen(config.port, () =>
  console.log(`Server listening on port ${config.port}!`)
);