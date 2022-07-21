from flask import Flask, abort, url_for, render_template, request, redirect, flash
from markupsafe import escape

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/")
def hello_world():
    app.logger.debug("Test debug text")
    app.logger.error("Test error text")
    app.logger.warning("Test warning text")
    return redirect(url_for("testi"))


@app.route("/index/<name>")
def home(name=None):
    return render_template("index.html", name=name)


@app.route("/test")
def test():
    return f"<p>Bello!</p>"


@app.route("/test/<username>")
def test2(username):
    return f"<p>Bello {escape(username)}!</p>"


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')
    else:
        return "<p>UPLOAD</p>"


@app.route("/testi")
def testi():
    abort(404)
    return "<p>Redirected!</p>"


# @app.route("/")
# def flashing():
#     # flash('You were successfully logged in')
#     return render_template('flashing.html')


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     flash("login please :-D")
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != 'admin' or \
#                 request.form['password'] != 'secret':
#             error = 'Invalid credentials'
#         else:
#             flash('You were successfully logged in')
#             return redirect(url_for('index'))
#     return render_template('login.html', error=error)


# @app.errorhandler(404)
# def not_found(error):
#     return f"<p>An error occured ({error})!</p>"


with app.test_request_context():
    print(url_for('static', filename='style.css'))
    print(url_for('test'))
    print(url_for('test', next='/'))
    print(url_for('test', username='John Doe'))
