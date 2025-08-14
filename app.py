from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def hello_world():
    return render_template('home.html')


@app.post("/post")
def get():
    return "Hello World"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6000, debug=True)
