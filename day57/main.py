from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    res = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("index.html", posts=res)

@app.route('/post/<int:id>')
def get_post(id):
    res = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("post.html", posts=res, id=id)


if __name__ == "__main__":
    app.run(debug=True)
