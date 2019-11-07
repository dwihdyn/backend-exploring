# `flask run` to deploy

import peeweedbevolve
from flask import Flask, render_template, request
from models import db

app = Flask(__name__)

# database setup
@app.before_request
def before_request():
    db.connect()


@app.after_request
def after_request(response):
    db.close()
    return response


# for migrate.py, `flask migrate` to run
@app.cli.command()
def migrate():
    db.evolve(ignore_tables={'base_model'})


# website directory
@app.route('/')
def index():
    store_name = request.args.get('store_name')
    return render_template("index.html", store_name=store_name)


if __name__ == "__main__":
    app.run()
