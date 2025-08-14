from flask import Flask

app = Flask(__name__)


@app.post("/")
def hello_world():
    return "hello World"


if __name__ == "__main__":
    print("I am inside")
    app.run(host='0.0.0.0', debug=True)

# Main Python application
print("Hello, Python!")


def main():
    print("Welcome to your Python development environment!")
