from flask import Flask, request
from flask.ext.bcrypt import Bcrypt
import settings
from database import db
import users


app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config.from_object('settings')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        users = db.session.query(user).filter(user.username == request.form['username']).first()
        if users is not None:
            pw_hash = bcrypt.generate_password_hash(user.password, 10)
            bcrypt.check_password_hash(pw_hash, user.password)
            return {"status": True}, "Autorizado"
            
        return {"status": False}, "Nao autorizado"


@app.route("/cadastrar", methods=['POST'])
def cadastrar():    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db.session.add(username, password)
        db.session.commit()

        return {"status": True}


if __name__ == '__main__':
    app.run(debug=True)