from flask import Flask, request, render_template
import subprocess
from random import randint
from hashlib import md5
import os
import re

app = Flask(__name__)


def xec(code):
    code = code.strip()
    indented = "\n".join(["    " + line for line in code.strip().splitlines()])

    file = f"/tmp/uploads/code_{md5(code.encode()).hexdigest()}.py"
    with open(file, 'w') as f:
        f.write("def main():\n")
        f.write(indented)
        f.write("""\nfrom parse import rgb_parse
print(rgb_parse(main()))""")

    os.system(f"chmod 755 {file}")

    try:
        res = subprocess.run(["sudo", "-u", "user", "python3", file],
                             capture_output=True, text=True, check=True, timeout=0.1)
        output = res.stdout
    except Exception as e:
        output = None

    os.remove(file)

    return output


@app.route('/', methods=["GET", "POST"])
def index():
    res = None
    if request.method == "POST":
        code = request.form["code"]
        res = xec(code)
        valid = re.compile(r"\([0-9]{1,3}, [0-9]{1,3}, [0-9]{1,3}\)")
        if res == None:
            return render_template("index.html", rgb=f"rgb({randint(0, 256)}, {randint(0, 256)}, {randint(0, 256)})")
        if valid.match("".join(res.strip().split("\n")[-1])):
            return render_template("index.html", rgb="rgb" + "".join(res.strip().split("\n")[-1]))
        return render_template("index.html", rgb=f"rgb({randint(0, 256)}, {randint(0, 256)}, {randint(0, 256)})")
    return render_template("index.html", rgb=f"rgb({randint(0, 256)}, {randint(0, 256)}, {randint(0, 256)})")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
