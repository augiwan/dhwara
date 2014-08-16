from flask import Flask
app = Flask(__name__)

@app.route("/signin")
def signin():
    return "Sign in!"

@app.route("/")
def dash():
    return "Jesus Christ!"

if __name__ == "__main__":
    app.debug = True
    app.run()
