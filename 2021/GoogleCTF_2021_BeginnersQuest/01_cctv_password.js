const checkPassword = () => {
    // const v = document.getElementById("password").value;
    const p = Array.from(v).map(a => 0xCafe + a.charCodeAt(0));

    if (p[0] === 52037 && p[6] === 52081 && p[5] === 52063 && p[1] === 52077 && p[9] === 52077 && p[10] === 52080 && p[4] === 52046 && p[3] === 52066 && p[8] === 52085 && p[7] === 52081 && p[2] === 52077 && p[11] === 52066) {
        window.location.replace(v + ".html");
    } else {
        alert("Wrong password!");
    }
}

let p = [];
p[0] = 52037;
p[6] = 52081;
p[5] = 52063;
p[1] = 52077;
p[9] = 52077;
p[10] = 52080;
p[4] = 52046;
p[3] = 52066;
p[8] = 52085;
p[7] = 52081;
p[2] = 52077;
p[11] = 52066;

let url = p.map( num => String.fromCharCode(num - 0xCafe)).join('');
console.log(url)