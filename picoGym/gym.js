function verify() {
    checkpass = document.getElementById("pass").value;
    split = 4;
    if (checkpass.substring(0, split) == 'pico') {
        if (checkpass.substring(split * 6, split * 7) == '723c') {
            if (checkpass.substring(split, split * 2) == 'CTF{') {
                if (checkpass.substring(split * 4, split * 5) == 'ts_p') {
                    if (checkpass.substring(split * 3, split * 4) == 'lien') {
                        if (checkpass.substring(split * 5, split * 6) == 'lz_7') {
                            if (checkpass.substring(split * 2, split * 3) == 'no_c') {
                                if (checkpass.substring(split * 7, split * 8) == 'e}') {
                                    alert("Password Verified")
                                }
                            }
                        }

                    }
                }
            }
        }
    }
    else {
        alert("Incorrect password");
    }

}

// picoCTF{no_clients_plz_7723ce}