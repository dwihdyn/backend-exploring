from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users/<user_name>')
def profile(user_name):
    return render_template("profile-page.html", username_profile_page=user_name)


if __name__ == '__main__':
    app.run(debug=True)
