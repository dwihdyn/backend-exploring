from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/users/<username>')
def profile(username):
    return render_template("profile_page.html", username=username)


@app.route('/checkout')
def checkout():
    return render_template("checkout_page.html")


if __name__ == "__main__":
    app.run(debug=True)
