from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/me')
def formexample():
    return 'Hello Me...'

@app.route('/lollipop')
def lolipop():
    return 'Sucking too hard on your lollipop,' \
           'Or love\'s gonna get you down....'
if __name__ == "__main__":
    app.run()
