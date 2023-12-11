from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlAlchemy import Usuario, Estado, Cidade, Endereco, Destinos, Origem, ClasseVoo, Passagem, Hotel, Hospedagem, UsuarioHasHospedagem, UsuarioHasPassagem
from sqlalchemy import or_, and_
from datetime import datetime
from sqlalchemy import func
from sqlalchemy import desc

engine = create_engine('postgresql://luanabrizola:qvkLUKZJ9Gd4@localhost:5432/TrabalhoBD4Bimestre')
#engine = create_engine('postgresql://postgres:postgres@localhost:5432/trabalho-bd')
Session = sessionmaker(bind=engine)
session = Session()


# DEFENDI CONSULTAS

# consultando hospedagens ordenando das mais baratas p as mais caras
resultado = session.query(Hospedagem).order_by(Hospedagem.precos.asc()).all()
for hospedagem in resultado:
    print(f"ID: {hospedagem.idhospedagem}, Preço: {hospedagem.precos}")

# consultando usuarios que foram para o hotel do estado id 5 ou 1
resultado = session.query(Usuario, Estado).join(UsuarioHasHospedagem, Usuario.cpf == UsuarioHasHospedagem.cpf).join(Hospedagem, UsuarioHasHospedagem.idhospedagem == Hospedagem.idhospedagem).join(Hotel, Hospedagem.idhotel == Hotel.idhotel).join(Endereco, Hotel.idendereco == Endereco.idendereco).join(Cidade, Endereco.idcidade == Cidade.idcidade).join(Estado, Cidade.idestado == Estado.idestado).filter(or_(Estado.idestado == '5', Estado.idestado == '1')).all()
for usuario, estado in resultado:
    print(f"CPF: {usuario.cpf}, ID estado: {estado.idestado}")

# usuarios que viajaram na classe 2 e escreveram a palavra "recomendo" em sua avaliação
resultado = session.query(Usuario, ClasseVoo, UsuarioHasPassagem).join(UsuarioHasPassagem, Usuario.cpf == UsuarioHasPassagem.cpf).join(Passagem, UsuarioHasPassagem.idpassagem == Passagem.idpassagem).join(ClasseVoo, Passagem.idclassevoo == ClasseVoo.idclassevoo).filter(and_(UsuarioHasPassagem.comentario.like("%recomendo%")), ClasseVoo.idclassevoo == 2)
for usuario, classe, comentario in resultado:
    print(f"CPF: {usuario.cpf}, id classe voo: {classe.idclassevoo}, comentario: {comentario.comentario}")

#LUANA CONSULTAS 

#Mostre os hotéis ordenados pelo número de quartos disponíveis em ordem decrescente.
resultado = session.query(Hotel).order_by(desc(Hotel.qtdequartos)).all()
for hotel in resultado:
    print(f"ID do Hotel: {hotel.idhotel}, Nome: {hotel.nome_hotel}, Quartos Disponíveis: {hotel.qtdequartos}")

#Mostre a média da hospedagem de cada hotel 
resultado = session.query(Hotel.nome_hotel, func.avg(Hospedagem.precos)).join(Hospedagem).group_by(Hotel.nome_hotel).all()
for hotel, media_precos in resultado:
    print(f"Nome do Hotel: {hotel}, Média de Preços de Hospedagens: {media_precos}")

#Mostre o id da hospedagem que tem como data de entrada e saida '2020-12-11' e '2020-12-15', respectivamente
data_inicio = datetime(202, 1, 11)
data_fim = datetime(2020, 12, 15)

resultado = session.query(Hospedagem).filter(Hospedagem.entrada.between(data_inicio, data_fim)).all()

for hospedagem in resultado:
    print(f"ID da Hospedagem: {hospedagem.idhospedagem}, Entrada: {hospedagem.entrada}, Saída: {hospedagem.saida}")