from sqlalchemy import create_engine, Column, Integer, String, Float, Date, Time, TIMESTAMP, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import create_engine


engine = create_engine('postgresql://postgres:postgres@localhost:5432/trabalho-bd')
# engine=create_engine('postgresql://luanabrizola:qvkLUKZJ9Gd4@ep-bold-flower-93463717.us-east-2.aws.neon.tech/TrabalhoBD4Bimestre')
#engine = create_engine('postgres/luanabrizola@TrabalhoBD4Bimestre')
conn = engine.connect()
print(engine)


Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()


class Usuario(Base):
    __tablename__ = 'usuario'
    cpf = Column(String(11), primary_key=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    senha = Column(String(15), nullable=False)

class Estado(Base):
    __tablename__ = 'estado'
    idestado = Column(Integer, primary_key=True)
    nome_estado = Column(String(100), nullable=False)

class Cidade(Base):
    __tablename__ = 'cidade'
    idcidade = Column(Integer, primary_key=True)
    nome_cidade = Column(String(100), nullable=False)
    idestado = Column(Integer, ForeignKey('estado.idestado'), nullable=False)
    estado = relationship('Estado', back_populates='cidades')

class Endereco(Base):
    __tablename__ = 'endereco'
    idendereco = Column(Integer, primary_key=True)
    rua = Column(String(50), nullable=False)
    numero = Column(String(6), nullable=False)
    idcidade = Column(Integer, ForeignKey('cidade.idcidade'), nullable=False)
    cidade = relationship('Cidade', back_populates='enderecos')

class Destinos(Base):
    __tablename__ = 'destinos'
    iddestino = Column(Integer, primary_key=True)
    descricao = Column(String(500), nullable=False)
    fotos = Column(String(20), nullable=False)
    idcidade = Column(Integer, ForeignKey('cidade.idcidade'), nullable=False)
    cidade = relationship('Cidade', back_populates='destinos')

class Origem(Base):
    __tablename__ = 'origem'
    idorigem = Column(Integer, primary_key=True)
    idendereco = Column(Integer, ForeignKey('endereco.idendereco'), nullable=False)
    endereco = relationship('Endereco', back_populates='origens')

class ClasseVoo(Base):
    __tablename__ = 'classevoo'
    idclassevoo = Column(Integer, primary_key=True)
    nomeclassevoo = Column(String(30), nullable=False)
    preco_classe = Column(Float)

class Passagem(Base):
    __tablename__ = 'passagem'
    idpassagem = Column(Integer, primary_key=True)
    data_ida = Column(TIMESTAMP, nullable=False)
    data_volta = Column(TIMESTAMP)
    idorigem = Column(Integer, ForeignKey('origem.idorigem'), nullable=False)
    origem = relationship('Origem', back_populates='passagens_origem')
    iddestino = Column(Integer, ForeignKey('destinos.iddestino'), nullable=False)
    destino = relationship('Destinos', back_populates='passagens_destino')
    duracao = Column(Time, nullable=False)
    companhia_aerea = Column(String(10), nullable=False)
    qtde_pessoas = Column(Integer, nullable=False)
    idclassevoo = Column(Integer, ForeignKey('classevoo.idclassevoo'), nullable=False)
    classevoo = relationship('ClasseVoo', back_populates='passagens')
    usuarios_passagem = relationship('UsuarioHasPassagem', back_populates='passagem')

class Hotel(Base):
    __tablename__ = 'hotel'
    idhotel = Column(Integer, primary_key=True)
    nome_hotel = Column(String(50))
    qtdehospedes = Column(Integer, nullable=False)
    qtdequartos = Column(Integer, nullable=False)
    idendereco = Column(Integer, ForeignKey('endereco.idendereco'), nullable=False)
    endereco_id = relationship('Endereco') 

    def get_endereco(self):
        return session.query(Endereco).get(self.idendereco)
    
class Hospedagem(Base):
    __tablename__ = 'hospedagem'
    idhospedagem = Column(Integer, primary_key=True)
    idhotel = Column(Integer, ForeignKey('hotel.idhotel'), nullable=False)
    hotel = relationship('Hotel', back_populates='hospedagens')
    precos = Column(Float, nullable=False)
    entrada = Column(Date, nullable=False)
    saida = Column(Date, nullable=False)
    usuarios_hospedagem = relationship('UsuarioHasHospedagem', back_populates='hospedagem')

class UsuarioHasHospedagem(Base):
    __tablename__ = 'usuario_has_hospedagem'
    cpf = Column(String(11), ForeignKey('usuario.cpf'), primary_key=True)
    usuario = relationship('Usuario', back_populates='hospedagens_usuario')
    idhospedagem = Column(Integer, ForeignKey('hospedagem.idhospedagem'), primary_key=True)
    hospedagem = relationship('Hospedagem', back_populates='usuarios_hospedagem')
    comentario = Column(String(500), nullable=False)

class UsuarioHasPassagem(Base):
    __tablename__ = 'usuario_has_passagem'
    cpf = Column(String(11), ForeignKey('usuario.cpf'), primary_key=True)
    usuario = relationship('Usuario', back_populates='passagens_usuario')
    idpassagem = Column(Integer, ForeignKey('passagem.idpassagem'), primary_key=True)
    passagem = relationship('Passagem', back_populates='usuarios_passagem')
    comentario = Column(String(500), nullable=False)


Estado.cidades = relationship('Cidade', back_populates='estado')
Cidade.enderecos = relationship('Endereco', back_populates='cidade')
Cidade.destinos = relationship('Destinos', back_populates='cidade')
Endereco.origens = relationship('Origem', back_populates='endereco')
Destinos.passagens_destino = relationship('Passagem', back_populates='destino')
Origem.passagens_origem = relationship('Passagem', back_populates='origem')
ClasseVoo.passagens = relationship('Passagem', back_populates='classevoo')
Hospedagem.usuarios_hospedagem = relationship('UsuarioHasHospedagem', back_populates='hospedagem')
Hospedagem.hotel = relationship('Hotel', back_populates='hospedagens')
Usuario.hospedagens_usuario = relationship('UsuarioHasHospedagem', back_populates='usuario')
Usuario.passagens_usuario = relationship('UsuarioHasPassagem', back_populates='usuario')
Passagem.usuarios_passagem = relationship('UsuarioHasPassagem', back_populates='passagem')
Hotel.hospedagens = relationship('Hospedagem', back_populates='hotel')

try:
    Base.metadata.create_all(engine)
except Exception as e:
    print(f"Erro ao criar tabelas: {e}")
