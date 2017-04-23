// function pasuser(form) {
//     if (form.id.value == "admin") {
//         if (x(form.pass.value) == "NeAM+bh_saaES_mFlSYYu}nYw}") {
//             location = "success.html"
//         } else {
//             alert("Invalid password/ID")
//         }
//     } else {
//         alert("Invalid UserID")
//     }
// }


// let password = "NeAM+bh_saaES_mFlSYYu}nYw}"
let password = "\u007fNeAM+bh_saaES_mFlSYYu}nYw}\u001d"
password = "IxSw{T^iEWWsei[pZeooCKXoA+K+"

function x(password) {
    var ASCII = [];
    var _0x9aadx5 = "";
    for (z = 1; z <= 255; z++) {
        ASCII[String["fromCharCode"](z)] = z
    }

    for (j = z = 0; z < password["length"]; z++) {
        _0x9aadx5 += String.fromCharCode(ASCII[password.substr(z,1)] ^ ASCII["6".substr(j, 1)]);
        console.log("char: ", password.substr(z,1), " : ", ASCII[password.substr(z,1)],

        " | XORed: ", ASCII[_0x9aadx5.substr(z,1)], String.fromCharCode(ASCII[password.substr(z,1)] ^ ASCII["6".substr(j, 1)]))

    }
    return _0x9aadx5
}

const res = x(password)
console.log(res)
console.log("passwd: ", password, " XORED: " , res, " :: NeAM+bh_saaES_mFlSYYu}nYw}")
if (res === "\u007fNeAM+bh_saaES_mFlSYYu}nYw}\u001d") {
    console.log("Password found! ", res)
}


/**
 * ORIGINAL SOURCE
 */
/*
function pasuser(form) {
    if (form.id.value == "admin") {
        if (x(form.pass.value, "6") == "NeAM+bh_saaES_mFlSYYu}nYw}") {
            location = "success.html"
        } else {
            alert("Invalid password/ID")
        }
    } else {
        alert("Invalid UserID")
    }
}
var functions = ["", "\x66\x72\x6F\x6D\x43\x68\x61\x72\x43\x6F\x64\x65", "\x6C\x65\x6E\x67\x74\x68", "\x73\x75\x62\x73\x74\x72"];


function x(password, "6") {
    var ASCII = [];
    var _0x9aadx5 = "";
    for (z = 1; z <= 255; z++) {
        ASCII[String["fromCharCode"](z)] = z
    }
    ; for (j = z = 0; z < password["length"]; z++) {
        _0x9aadx5 += String["fromCharCode"](ASCII[password["substr"](z, 1)] ^ ASCII["6"["substr"](j, 1)]);
        j = (j < "6"["length"]) ? j + 1 : 0
    }
    ; return _0x9aadx5
}
*/