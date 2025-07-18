from flask import *
from os import *
from bot import *  
from urllib.parse import *
app=Flask(__name__)

app.config["SECRET_KEY"]=urandom(32)


@app.route("/", methods=["POST", "GET"])
def note():
    return render_template("notes.html")


@app.route("/report", methods=["GET", "POST"])
def report():
    if request.method == "GET":
        return render_template("visit.html")
    bot = Bot()
    url = request.form.get('url')
    if url:
        try:
            parsed_url = urlparse(url)
        except Exception:
            return {"error": "Invalid URL."}, 400

        if parsed_url.scheme not in ["http", "https"]:
            return {"error": "Invalid scheme."}, 400

        bot.visit(url)
        bot.close()
        return {"visited": url}, 200
    else:
        return {"error": "URL parameter is missing!"}, 400

if __name__=="__main__":
    app.run(host="0.0.0.0", port=3000)
