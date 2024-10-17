from flask import Flask, session, redirect, flash, request, url_for
from controllers.test import hello_controller

app = Flask(__name__)
app.register_blueprint(hello_controller)
app.secret_key = 'chave'

if __name__ == '__main__':
    app.run(debug=True)