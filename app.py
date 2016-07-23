#!usr/bin/python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import views

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://larrisa:postgres@localhost/flaskmovie'
app.debug = True
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run()
