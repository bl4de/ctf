import os,string,sqlite3
import binascii
from base64 import b64encode
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'alphabet.db'),
    SECRET_KEY=os.urandom(32)
))

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

def valid_input(inp):
    whitelist = string.ascii_letters+string.digits+" \n\r"
    if len(inp) == 0 or len(inp) > 1600:
        return False
    for c in inp:
        if not c in whitelist:
            return False
    return True

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""  
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/view/<title>')
def view_page(title):
    if not valid_input(title):
        abort(404)
    db = get_db()
    cur = db.execute("SELECT type, content FROM pages WHERE title='%s'" % title)
    page = cur.fetchone()
    if not page:
        abort(404)
    elif page['type'] == 'art':
        return render_template('view_art.html', title=title, art=page['content'])
    elif page['type'] == 'album':
        cur = db.execute("SELECT title, content FROM pages WHERE title IN (%s)" % page['content'])
        arts = cur.fetchall()
        return render_template('view_album.html', title=title, arts=arts)

@app.route('/edit/<title>', methods=['GET', 'POST'])
def edit_art(title):
    if not valid_input(title):
        abort(404)
    if not 'arts' in session or not title in session['arts']:
        abort(403)
    db = get_db()
    if request.method == 'POST':
        art_data = request.form['art_data']
        if not valid_input(art_data):
            return render_template('error.html', error='No hacker characters allowed!!')
        db.execute("UPDATE pages SET content='%s' WHERE title='%s'" % (art_data, title))
        db.commit()
        return redirect(url_for('view_page', title=title))
    else:
        cur = db.execute("SELECT content FROM pages WHERE title='%s'" % title)
        page = cur.fetchone()
        return render_template('edit_art.html', title=title, art=page['content'])
        

@app.route('/create_album', methods=['GET','POST'])
def create_album():
    if request.method == 'GET':
        return render_template('create_album.html')
    title = request.form['title']
    if not valid_input(title):
        return render_template('error.html', error='No hacker characters allowed!!')
    db = get_db()
    if db.execute("SELECT 1 FROM pages WHERE title='%s'" % title).fetchone():
        return render_template('error.html', error='Title already in use')
    arts = request.form.getlist('arts')
    for i in arts:
        if not valid_input(i):
            return render_template('error.html', error='Art does not exist')
        cur = db.execute("SELECT content FROM pages WHERE type='art' AND title='%s'" % i)
        page = cur.fetchone()
        if not page:
             return render_template('error.html', error='Art does not exist')
    album_data = "''"+"'',''".join(arts)+"''"
    db.execute("INSERT INTO pages (title,type,content) VALUES ('%s','album','%s')" % (title,album_data))
    db.commit()
    return redirect(url_for('view_page',title=title))
    
@app.route('/share', methods=['POST'])
def create_art():
    title = request.form['title']
    art_data = request.form['art_data']
    if not valid_input(title) or not valid_input(art_data):
        return render_template('error.html', error='No hacker characters allowed!!' )
    db = get_db()
    if db.execute("SELECT 1 FROM pages WHERE title='%s'" % title).fetchone():
        return render_template('error.html', error='Title already in use')
    db.execute("INSERT INTO pages (title,type,content) VALUES ('%s','art','%s')" % (title,art_data))
    db.commit()
    if 'arts' in session:
        session['arts'] += [title]
    else:
        session['arts'] = [title]
    return redirect(url_for('view_page',title=title))

@app.route('/delete/<title>')
def delete_art(title):
    if not valid_input(title):
        abort(404)
    if not 'arts' in session or not title in session['arts']:
        abort(403)
    db = get_db()
    db.execute("DELETE FROM pages WHERE title='%s'" % title)
    db.commit()
    session['arts'].remove(title)
    session.modified=True
    return redirect(url_for('home'))
