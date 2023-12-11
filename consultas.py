from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlAlchemy import Usuario, Estado, Cidade, Endereco, Destinos, Origem, ClasseVoo, Passagem, Hotel, Hospedagem, UsuarioHasHospedagem, UsuarioHasPassagem
from datetime import date
from sqlalchemy import or_, and_

engine = create_engine('postgresql://postgres:postgres@localhost:5432/trabalho-bd')
Session = sessionmaker(bind=engine)
session = Session()


# DEFENDI CONSULTAS

# consultando hospedagens ordenando das mais baratas p as mais caras
hospedagensordenadas = session.query(Hospedagem).order_by(Hospedagem.precos.asc()).all()
for hospedagem in hospedagensordenadas:
    print(f"ID: {hospedagem.idhospedagem}, Preço: {hospedagem.precos}")

# consultando usuarios que foram para o hotel do estado id 5 ou 1
resultado = session.query(Usuario, Estado).join(UsuarioHasHospedagem, Usuario.cpf == UsuarioHasHospedagem.cpf).join(Hospedagem, UsuarioHasHospedagem.idhospedagem == Hospedagem.idhospedagem).join(Hotel, Hospedagem.idhotel == Hotel.idhotel).join(Endereco, Hotel.idendereco == Endereco.idendereco).join(Cidade, Endereco.idcidade == Cidade.idcidade).join(Estado, Cidade.idestado == Estado.idestado).filter(or_(Estado.idestado == '5', Estado.idestado == '1')).all()
for usuario, estado in resultado:
    print(f"CPF: {usuario.cpf}, ID estado: {estado.idestado}")

# usuarios que viajaram na classe 2 e escreveram a palavra "recomendo" em sua avaliação
resultado = session.query(Usuario, ClasseVoo, UsuarioHasPassagem).join(UsuarioHasPassagem, Usuario.cpf == UsuarioHasPassagem.cpf).join(Passagem, UsuarioHasPassagem.idpassagem == Passagem.idpassagem).join(ClasseVoo, Passagem.idclassevoo == ClasseVoo.idclassevoo).filter(and_(UsuarioHasPassagem.comentario.like("%recomendo%")), ClasseVoo.idclassevoo == 2)
for usuario, classe, comentario in resultado:
    print(f"CPF: {usuario.cpf}, id classe voo: {classe.idclassevoo}, comentario: {comentario.comentario}")