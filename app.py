from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///viagens.db'
db = SQLAlchemy(app)


class Usuario(db.Model):
    cpf = db.Column(db.String(11), primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(15), nullable=False)

class Estado(db.Model):
    idestado = db.Column(db.Integer, primary_key=True)
    nome_estado = db.Column(db.String(100), nullable=False)

class Cidade(db.Model):
    idecidaade = db.Column(db.Integer, primary_key=True)
    nome_cidade = db.Column(db.String(100), nullable=False)
    idestado = db.Column(db.Integer, db.ForeignKey('estado.idestado'), nullable=False)
    estado = db.relationship('Estado', backref=db.backref('cidades', lazy=True))
    

# Rota principal
@app.route('/')
def index():
    return 'Bem-vindo ao aplicativo de viagens!'

# Rota para listar todos os usuários
@app.route('/usuarios')
def listar_usuarios():
    usuarios = Usuario.query.all()
    return render_template('listar_usuarios.html', usuarios=usuarios)

# Rota para listar todos os estados
@app.route('/estados')
def listar_estados():
    estados = Estado.query.all()
    return render_template('listar_estados.html', estados=estados)


#if __name__ == '__main__':
#   app.run(debug=True)
