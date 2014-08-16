from flask import Flask, render_template
app = Flask(__name__)

@app.route("/signin")
def signin():
    return render_template('signin.jinja2')

@app.route("/")
def dash():
    return render_template('dashboard.jinja2')

if __name__ == "__main__":
    app.debug = True
    app.run()
