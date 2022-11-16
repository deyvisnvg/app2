from flask import Flask, render_template, redirect, flash, url_for
from config import Config
from models.forms.loginmodel import LoginForm
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/unaRuta")
def unaRuta():
    info = "Hola"
    return render_template("unaRuta.html", data=info)


lista = ['a', 'b', 'c']


@app.route("/iterando")
def iterando():
    return render_template('iterando.html', letras=lista)


@app.route("/login", methods=['GET', 'POST'])
def login():
    formulario = LoginForm()
    if formulario.validate_on_submit():
        flash('Inicio de Sesión solicitado por {}, ¿Recordarme?={}'.format(
            formulario.username.data, formulario.remember_me.data))
        return redirect(url_for('indexcss'))

    return render_template("login.html", form=formulario)


@app.route("/css")
def indexcss():
    return render_template("indexcss.html")


if __name__ == '__main__':
    app.run(debug=True)
