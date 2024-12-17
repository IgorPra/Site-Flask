from flask import Flask
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///dados.db"


db.init_app(app)


from routes import *

if __name__ == '__main__':
    with app.app_context():

       db.create_all()
    app.run(debug=True)
    input("Aperte enter apenas quando vc clicar no link")