from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    # first_name & last_name objects needed, so that we can print it out once user has fill up the contact-us
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    return render_template("index.html", first_name=first_name, last_name=last_name)


# check other users in navbar
@app.route('/users/<user_name>')
def profile(user_name):
    return render_template("profile-page.html", username_profile_page=user_name)


# dont need objects, because we dont want to store the input data to any database (since no db exist) for now
@app.route('/contact-us')
def contact():
    return render_template("contact-us.html")


if __name__ == '__main__':
    app.run(debug=True)
