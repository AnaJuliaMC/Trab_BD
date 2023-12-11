from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/trabalho-bd'
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
    idcidade = db.Column(db.Integer, primary_key=True)  # Corrigido o nome da coluna
    nome_cidade = db.Column(db.String(100), nullable=False)
    idestado = db.Column(db.Integer, db.ForeignKey('estado.idestado'), nullable=False)
    estado = db.relationship('Estado', backref=db.backref('cidades', lazy=True))

class Endereco(db.Model):
    idendereco = db.Column(db.Integer, primary_key=True)
    rua = db.Column(db.String(50), nullable=False)
    numero = db.Column(db.String(6), nullable=False)
    idcidade = db.Column(db.Integer, db.ForeignKey('cidade.idcidade'), nullable=False)
    cidade = db.relationship('Cidade', backref=db.backref('enderecos', lazy=True))

class Destinos(db.Model):
    iddestino = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(500), nullable=False)
    fotos = db.Column(db.String(20), nullable=False)
    idcidade = db.Column(db.Integer, db.ForeignKey('cidade.idcidade'), nullable=False)
    cidade = db.relationship('Cidade', backref=db.backref('destinos', lazy=True))

class Origem(db.Model):
    idorigem = db.Column(db.Integer, primary_key=True)
    idendereco = db.Column(db.Integer, db.ForeignKey('endereco.idendereco'), nullable=False)
    endereco = db.relationship('Endereco', backref=db.backref('origens', lazy=True))

class ClasseVoo(db.Model):
    __tablename__ = 'classevoo'
    idclassevoo = db.Column(db.Integer, primary_key=True)
    nomeclassevoo = db.Column(db.String(30), nullable=False)
    preco_classe = db.Column(db.Float)

class Passagem(db.Model):
    idpassagem = db.Column(db.Integer, primary_key=True)
    data_ida = db.Column(db.TIMESTAMP, nullable=False)
    data_volta = db.Column(db.TIMESTAMP)
    idorigem = db.Column(db.Integer, db.ForeignKey('origem.idorigem'), nullable=False)
    origem = db.relationship('Origem', backref=db.backref('passagens_origem', lazy=True))
    iddestino = db.Column(db.Integer, db.ForeignKey('destinos.iddestino'), nullable=False)
    destino = db.relationship('Destinos', backref=db.backref('passagens_destino', lazy=True))
    duracao = db.Column(db.Time, nullable=False)
    companhia_aerea = db.Column(db.String(10), nullable=False)
    qtde_pessoas = db.Column(db.Integer, nullable=False)
    idclassevoo = db.Column(db.Integer, db.ForeignKey('classevoo.idclassevoo'), nullable=False)
    classevoo = db.relationship('ClasseVoo', backref=db.backref('passagem', lazy=True))

class Hotel(db.Model):
    idhotel = db.Column(db.Integer, primary_key=True)
    nome_hotel = db.Column(db.String(50))
    qtdehospedes = db.Column(db.Integer, nullable=False)
    qtdequartos = db.Column(db.Integer, nullable=False)
    idendereco = db.Column(db.Integer, db.ForeignKey('endereco.idendereco'), nullable=False)
    endereco_id = db.relationship('Endereco') 

    def get_endereco(self):
        return db.session.query(Endereco).get(self.idendereco)
    
class Hospedagem(db.Model):
    idhospedagem = db.Column(db.Integer, primary_key=True)
    idhotel = db.Column(db.Integer, db.ForeignKey('hotel.idhotel'), nullable=False)
    hotel = db.relationship('Hotel', backref=db.backref('hospedagem', lazy=True))
    precos = db.Column(db.Float, nullable=False)
    entrada = db.Column(db.Date, nullable=False)
    saida = db.Column(db.Date, nullable=False)
    # usuarios_hospedagem = db.relationship('UsuarioHasHospedagem', back_populates='hospedagem')

class UsuarioHasPassagem(db.Model):
    __tablename__ = 'usuario_has_passagem'
    cpf = db.Column(db.String(11), db.ForeignKey('usuario.cpf'), primary_key=True)
    usuario = db.relationship('Usuario', backref=db.backref('passagens_usuario', lazy=True))
    idpassagem = db.Column(db.Integer, db.ForeignKey('passagem.idpassagem'), primary_key=True)
    passagem = db.relationship('Passagem', backref=db.backref('usuarios_passagem', lazy=True))
    comentario = db.Column(db.String(500), nullable=False)

class UsuarioHasHospedagem(db.Model):
    __tablename__ = 'usuario_has_hospedagem'
    cpf = db.Column(db.String(11), db.ForeignKey('usuario.cpf'), primary_key=True)
    usuario = db.relationship('Usuario', backref=db.backref('hospedagens_usuario', lazy=True))
    idhospedagem = db.Column(db.Integer, db.ForeignKey('hospedagem.idhospedagem'), primary_key=True)
    hospedagem = db.relationship('Hospedagem', backref=db.backref('usuarios_hospedagem', lazy=True))
    comentario = db.Column(db.String(500), nullable=False)

# Rota principal
@app.route('/')
def index():
    return 'Bem-vindo ao aplicativo de viagens!'

# Rota para listar todos os usuários
@app.route('/usuarios')
def listar_usuarios():
    usuarios = Usuario.query.all()
    return render_template('usuarios.html', usuarios=usuarios)

# Rota para listar todos os estados
@app.route('/estados')
def listar_estados():
    estados = Estado.query.all()
    return render_template('estados.html', estados=estados)

@app.route('/cidades')
def listar_cidades():
    cidades = Cidade.query.all()
    return render_template('cidades.html', cidades=cidades)

@app.route('/enderecos')
def listar_enderecos():
    enderecos = Endereco.query.all()
    return render_template('enderecos.html', enderecos=enderecos)

@app.route('/destinos')
def listar_destinos():
    destinos = Destinos.query.all()
    return render_template('destinos.html', destinos=destinos)

@app.route('/origens')
def listar_origens():
    origens = Origem.query.all()
    return render_template('origens.html', origens=origens)

@app.route('/classes')
def listar_classes():
    classes = ClasseVoo.query.all()
    return render_template('classes.html', classes=classes)

@app.route('/passagens')
def listar_passagens():
    passagens = Passagem.query.all()
    return render_template('passagens.html', passagens=passagens)

@app.route('/hoteis')
def listar_hoteis():
    hoteis = Hotel.query.all()
    return render_template('hoteis.html', hoteis=hoteis)

@app.route('/hospedagens')
def listar_hospedagens():
    hospedagens = Hospedagem.query.all()
    return render_template('hospedagens.html', hospedagens=hospedagens)

@app.route('/usupassagens')
def listar_usupassagens():
    usupassagens = UsuarioHasPassagem.query.all()
    return render_template('usupassagens.html', usupassagens=usupassagens)

@app.route('/usuhospedagens')
def listar_usuhospedagens():
    usuhospedagens = UsuarioHasHospedagem.query.all()
    return render_template('usuhospedagens.html', usuhospedagens=usuhospedagens)

if __name__ == '__main__':
    app.run(debug=True)
