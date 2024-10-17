from flask import Blueprint, request, url_for, redirect, render_template, session, flash
from models.usuario import User

Adm = User("ADM", "senhaforte")
Usuario1 = User("peixe", "1234")
lista = [Adm, Usuario1]

hello_controller = Blueprint('hello', __name__)


@hello_controller.route('/', methods=['POST', 'GET'])
def index():
    usuario_logado = session.get('usuario_logado')
    return render_template('home.html', usuario=usuario_logado)

@hello_controller.before_request
def autenticar_usuario():

    rota_protegida = request.endpoint in ['hello.protected']

    if rota_protegida and 'usuario_logado' not in session:
        flash("Você precisa estar logado para acessar essa página.")
        return redirect(url_for('hello.login'))

# parte de login

@hello_controller.route('/login', methods=['POST', 'GET'])
def login():
    # lógica?
    if request.method == "POST":
        session['usuario'] = request.form['username']
        return redirect(url_for('hello.index'))
    return render_template('login.html')

@hello_controller.route('/autenticar', methods=["POST"])
def autenticar():
    username = request.form['username']
    password = request.form['password']

    for usuario in lista:
        if usuario.validate(username, password):
            session['usuario_logado'] = usuario.username
            flash(f'{usuario.username} logado com sucesso!')
            return redirect(url_for('hello.index'))

    flash('Usuário ou senha incorretos.')
    return redirect(url_for('hello.login'))
   
@hello_controller.route('/logout')
def logout():
    session.pop('usuario_logado', None)
    return redirect(url_for('hello.login'))