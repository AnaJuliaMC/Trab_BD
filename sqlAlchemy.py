from sqlalchemy import Column, Integer, String
from email.mime import base
from sqlalchemy.orm import declarative_base
base = declarative_base()


class usuario(base):
    __tablename__ = 'usuario'

    cpf = Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String)
    senha = Column(String)

    def __repr__(Self):
        return "< usuario(nome=’%s ’, email=’%s ’, senha=’%s ’) > " % (
            self .nome, self .sobrenome, self .senha)


class estado(base):
    __tablename__ = 'estado'

    idestado = Column(Integer, primary_key=True)
    nome_estado = Column(String)

    def __repr__(Self):
        return "< estado(nome_estado=’%s ’) > " % (
            self .nome_estado)


class cidade(base):
    __tablename__ = 'cidade'

    id= Column(Integer, primary_key=True)
    nome_cidade = Column(String)
    idestado = Column(Integer, ForeignKey('estado.id'))

    def __repr__(Self):
        return "< cidade(nome_cidade=’%s ’) > " % (
            self .nome_cidade)


class endereco(base):
    __tablename__ = 'endereco'

    id = Column(Integer, primary_key=True)
    rua = Column(String)
    numero = Column(Integer)
    idcidade = Column(Integer, ForeignKey('cidade.id'))

    def __repr__(Self):
        return "< endereco (rua=’%s ’, numero=’%s ’) > " % (
            self .rua, self .numero)

class destinos(base):
    __tablename__ = 'destinos'

    id = Column(Integer, primary_key=True)
    decricao = Column(String)
    foto = Column(Integer)
    idcidade = Column(Integer,ForeignKey('cidade.id'))

    def __repr__(Self):
        return "< destino (descricao=’%s ’, foto=’%s ’) > " % (
            self .descricao, self .foto)

class origem(base):
    __tablename__ = 'origem'

    id = Column(Integer, primary_key=True)
    idendereco = Column(Integer, foreign_key=True)


