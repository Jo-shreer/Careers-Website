from flask import Flask

app = Flask(__name__)


@app.post("/post")
def hello_world():
    return "hello World"


@app.get("/")
def get():
    return "Hello World"


if __name__ == "__main__":
    print("I am inside")
    app.run(host='0.0.0.0', port=6000, debug=True)
