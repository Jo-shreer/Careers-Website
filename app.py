from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'Title': 'Python Developer',
    'Location': 'Dublin',
    'Salary': '50k'
}, {
    'id': 2,
    'Title': 'Full Stack Developer',
    'Location': 'Dublin',
    'Salary': '70k'
}, {
    'id': 3,
    'Title': 'Backend Developer',
    'Location': 'Dublin',
    'Salary': '70k'
}]


@app.get("/")
def hello_world():
    return render_template('home.html', jobs=JOBS)


@app.post("/post")
def get():
    return "Hello World"


@app.route("/api/jobs")
def getall():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6000, debug=True)
