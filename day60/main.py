from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/login", methods=["POST"])
def receive_info():
    if request.method == 'POST':
        return f"<h1>Name: {request.form['username']}, Password: {request.form['password']}"

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)