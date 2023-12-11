from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlAlchemy import Usuario, Estado, Cidade, Endereco, Destinos, Origem, ClasseVoo, Passagem, Hotel, Hospedagem, UsuarioHasHospedagem, UsuarioHasPassagem
from datetime import date

engine = create_engine('postgresql://postgres:postgres@localhost:5432/trabalho-bd')
Session = sessionmaker(bind=engine)
session = Session()

# INSERINDO USUARIOS
usuarios = [
    Usuario(cpf='12345676543', nome='Ana Silva', email='anasilva@gmail.com', senha='anasilva123'),
    Usuario(cpf='3334445556', nome='Juliana Rocha', email='jurocha@gmail.com', senha='amogatos123'),
    Usuario(cpf='1234567891', nome='Larissa Ramos', email='larilinda@gmail.com', senha='larizinhaah'),
    Usuario(cpf='5556667778', nome='Eduardo Pena', email='edupena@gmail.com', senha='edupena1'),
    Usuario(cpf='11587806988', nome='Hiago Gimenez', email='giagimenez1@gmail.com', senha='hiago88'),
    Usuario(cpf='15142365890', nome='João Bühler', email='ruivinho1@gmail.com', senha='ruivodamene'),
    Usuario(cpf='19892345726', nome='Maria Menezes', email='mariam123@gmail.com', senha='210492'),
    Usuario(cpf='83561809264', nome='Marcela Viera', email='vierama@gmail.com', senha='ferrari'),
    Usuario(cpf='19027198913', nome='Ana Almeida', email='almeidaana13@gmail.com', senha='taylorswift13'),
    Usuario(cpf='11122233387', nome='Maisa Silva', email='maisasilvaofc@gmail.com', senha='silvamah1'),
    Usuario(cpf='29876587621', nome='Flavia Reitz', email='flaviareitz@gmail.com', senha='farc78'),
    Usuario(cpf='56789123455', nome='Luana Cardoso', email='luaninha@gmail.com', senha='luluzinha'),
    Usuario(cpf='45321168876', nome='Maria Julia Rodrigues', email='jujumaria@gmail.com', senha='senhadificil11'),
    Usuario(cpf='23454314522', nome='João Augusto Costa', email='jaugust@gmail.com', senha='viajante1'),
    Usuario(cpf='78956432144', nome='Matheus Lima', email='lmatt@gmail.com', senha='soulindo1'),
    Usuario(cpf='21343255565', nome='Larissa Manoela', email='larimanu@gmail.com', senha='laricell11'),
    Usuario(cpf='32155547899', nome='Karina Costa', email='familiaviajante@gmail.com', senha='viajante2'),
    Usuario(cpf='44355688921', nome='Virginia Fonseca', email='fonsecav@gmail.com', senha='maedasmarias'),
    Usuario(cpf='15678955567', nome='Luiz Marcio Nogueira', email='marcinho@gmail.com', senha='luizinhom12'),
    Usuario(cpf='23454366654', nome='Luciah Sophie Pereira', email='luciacomh@gmail.com', senha='luciahsophie')
]

# INSERINDO OS ESTADOS
estados = [
    Estado(idestado=1, nome_estado='Rio de Janeiro'),
    Estado(idestado=2, nome_estado='Rio Grande do Sul'),
    Estado(idestado=3, nome_estado='Maranhão'),
    Estado(idestado=4, nome_estado='Paraná'),
    Estado(idestado=5, nome_estado='São Paulo'),
    Estado(idestado=6, nome_estado='Bahia'),
    Estado(idestado=7, nome_estado='Mato Grosso do Sul'),
    Estado(idestado=8, nome_estado='Tocantins'),
    Estado(idestado=9, nome_estado='Paraíba'),
    Estado(idestado=10, nome_estado='Alagoas'),
    Estado(idestado=11, nome_estado='Santa Catarina')
]

# INSERINDO AS CIDADES
cidades = [
    Cidade(idcidade=1, nome_cidade='Rio de Janeiro', idestado=1),
    Cidade(idcidade=2, nome_cidade='Gramado', idestado=2),
    Cidade(idcidade=3, nome_cidade='Barreirinhas', idestado=3),
    Cidade(idcidade=4, nome_cidade='Curitiba', idestado=4),
    Cidade(idcidade=5, nome_cidade='São Paulo', idestado=5),
    Cidade(idcidade=6, nome_cidade='Foz do Iguaçu', idestado=4),
    Cidade(idcidade=7, nome_cidade='Porto Seguro', idestado=6),
    Cidade(idcidade=8, nome_cidade='Bonito', idestado=7),
    Cidade(idcidade=9, nome_cidade='Mateiros', idestado=8),
    Cidade(idcidade=10, nome_cidade='Campos do Jordão', idestado=5),
    Cidade(idcidade=11, nome_cidade='João Pessoa', idestado=9),
    Cidade(idcidade=12, nome_cidade='Maceió', idestado=10),
    Cidade(idcidade=13, nome_cidade='Florianópolis', idestado=11),
    Cidade(idcidade=14, nome_cidade='Maringá', idestado=4)
]

# INSERINDO OS ENDEREÇOS
enderecos = [
    Endereco(idendereco=1, rua='Rua das Flores', numero='311', idcidade=12),
    Endereco(idendereco=2, rua='Rua Maringa', numero='21', idcidade=14),
    Endereco(idendereco=3, rua='Rua Girassol', numero='01', idcidade=1),
    Endereco(idendereco=4, rua='Rua Goias', numero='411', idcidade=6),
    Endereco(idendereco=5, rua='Rua São Paulo', numero='2012', idcidade=14),
    Endereco(idendereco=6, rua='Rua Pato Branco', numero='267', idcidade=14),
    Endereco(idendereco=7, rua='Rua Evermore', numero='13', idcidade=10),
    Endereco(idendereco=8, rua='Rua Beltrão', numero='127', idcidade=9),
    Endereco(idendereco=9, rua='Rua das Araras', numero='31', idcidade=8),
    Endereco(idendereco=10, rua='Rua da Fama', numero='189', idcidade=5),
    Endereco(idendereco=11, rua='Rua Amores', numero='25', idcidade=3),
    Endereco(idendereco=12, rua='Avenida Principal', numero='890', idcidade=6),
    Endereco(idendereco=13, rua='Rua das Casinhas', numero='900', idcidade=7),
    Endereco(idendereco=14, rua='Rua Girassol', numero='23', idcidade=13),
    Endereco(idendereco=15, rua='Avenida Joao Pessoa', numero='77', idcidade=12),
    Endereco(idendereco=16, rua='Rua da Fama', numero='155', idcidade=1),
    Endereco(idendereco=17, rua='Avenida dos Empresarios', numero='89', idcidade=5),
    Endereco(idendereco=18, rua='Rua Cianorte', numero='601', idcidade=2),
    Endereco(idendereco=19, rua='Avenida da Paz', numero='311', idcidade=11),
    Endereco(idendereco=20, rua='R. Anacleto de Carvalho', numero='475', idcidade=3),
    Endereco(idendereco=21, rua='R. Tirol', numero='149', idcidade=2),
    Endereco(idendereco=22, rua='Av. Rebouças', numero='955', idcidade=5),
    Endereco(idendereco=23, rua='Av. Atlântica', numero='1702', idcidade=1),
    Endereco(idendereco=24, rua='Praça Gen. Osório', numero='61', idcidade=4),
    Endereco(idendereco=25, rua='R. Machado Lemos', numero='433', idcidade=12),
    Endereco(idendereco=26, rua='R. Mariano Torres', numero='976', idcidade=4),
    Endereco(idendereco=27, rua='R. do Cajueiro', numero='5', idcidade=7),
    Endereco(idendereco=28, rua='R. Nossa Sra. da Penha', numero='366', idcidade=8),
    Endereco(idendereco=29, rua='Av. Gov. Argemiro de Figueiredo', numero='3197', idcidade=11),
    Endereco(idendereco=30, rua='Avenida Costa e Silva', numero='154', idcidade=6)
]

# INSERINDO AS ORIGENS
origens = [
    Origem(idorigem=1, idendereco=19),
    Origem(idorigem=2, idendereco=17),
    Origem(idorigem=3, idendereco=16),
    Origem(idorigem=4, idendereco=15),
    Origem(idorigem=5, idendereco=14),
    Origem(idorigem=6, idendereco=13),
    Origem(idorigem=7, idendereco=12),
    Origem(idorigem=8, idendereco=10),
    Origem(idorigem=10, idendereco=9),
    Origem(idorigem=11, idendereco=8),
    Origem(idorigem=12, idendereco=6),
    Origem(idorigem=13, idendereco=4),
    Origem(idorigem=14, idendereco=3),
    Origem(idorigem=15, idendereco=1)
]

# INSERINDO OS DESTINOS
destinos = [
    Destinos(iddestino=1, descricao='Existem vários motivos que fazem do Rio um dos cartões postais brasileiros mais conhecidos em todo o mundo, e suas belas praias com certeza são um deles! Copacabana, Ipanema, Leblon, Praia do Arpoador e muitas outras contornam a cidade maravilhosa como a moldura perfeita', fotos='riodejaneiro123.png', idcidade=1),
    Destinos(iddestino=2, descricao='Gramado é a principal cidade da Serra Gaúcha e sem dúvidas é um dos melhores destinos turísticos do país. Romântica, charmosa, cheia de cultura, belas paisagens, atrações e ótima culinária, Gramado é capaz de agradar a todos e sempre oferece novas opções.', fotos='gramado321.png', idcidade=2),
    Destinos(iddestino=3, descricao='Mais uma vez a beleza natural aparecendo na lista das atrações surpreendentes do Nordeste brasileiro. Com lindas lagoas, dunas brancas e um ecossistema único, aqui é possível conferir de perto um dos mais belos conjuntos de paisagens do país.', fotos='lencoismaa.png', idcidade=3),
    Destinos(iddestino=4, descricao='A cidade de Curitiba, capital do estado do Paraná, é conhecida pelo cuidado com o planejamento urbano, belas áreas verdes e um transporte público de qualidade. A fama não é para menos. Curitiba realmente oferece um excelente padrão de vida para os moradores.', fotos='curitiba2.png', idcidade=4),
    Destinos(iddestino=5, descricao='São Paulo, centro financeiro do Brasil, está entre as cidades mais populosas do mundo, com diversas instituições culturais e uma rica tradição arquitetônica.', fotos='saopaulo.png', idcidade=5),
    Destinos(iddestino=6, descricao='Foz do Iguaçu é uma cidade turística que fica no sul do Brasil, conhecida pelas Cataratas do Iguaçu, por fazer fronteira com Paraguai e Argentina, pelos hotéis e pousadas e seus ambientes familiares, e por estar se tornando um polo de parques temáticos no Brasil.', fotos='cataratasfoz.png', idcidade=6),
    Destinos(iddestino=7, descricao='Porto Seguro é um dos destinos de praia preferidos no Brasil, em virtude de suas belíssimas praias, da farta rede hoteleira e por ser o destino mais próximo do Nordeste para quem mora no Sul e Sudeste do país.', fotos='portoseguro.png', idcidade=7),
    Destinos(iddestino=8, descricao='Bonito é considerado um dos melhores destinos de ecoturismo do Brasil, por causa da beleza de seus atrativos, mas também da forma rigorosa como são preservados.', fotos='bonito.png', idcidade=8),
    Destinos(iddestino=9, descricao='Mateiros é o verdadeiro paraíso em meio ao cerrado brasileiro. Lá você encontrará diversas atividades ao ar livre que te encantarão.', fotos='parquejalapao.png', idcidade=9),
    Destinos(iddestino=10, descricao='Campos do Jordão é um dos destinos queridinhos do Brasil, ótima opção o ano inteiro, principalmente no inverno! É um lugar cercado pelo charme das montanhas, influenciado pela cultura europeia, cheio de restaurantes e atividades para pessoas de todas as idades.', fotos='camposjordao.png', idcidade=10),
    Destinos(iddestino=11, descricao='Viajar para João Pessoa é encontrar praias maravilhosas e um povo muito receptivo e orgulhoso de sua região. Aposte na Paraíba, e você não vai se arrepender.', fotos='joaopessoa1.png', idcidade=11),
    Destinos(iddestino=12, descricao='Maceió, tem um jeitinho de cidade do interior e ritmo menos acelerado do que outras capitais brasileiras, e esse é um de seus grandes charmes. Os turistas que a visitam contam com restaurantes de qualidade, bons hotéis, além de ótimas praias e diversidade de passeios.', fotos='maceio.png', idcidade=12),
    Destinos(iddestino=13, descricao='Conhecida como Ilha da Magia e carinhosamente chamada de Floripa, cada pedacinho de Florianópolis tem uma característica distinta, sendo sempre sua principal atração a Natureza, especialmente através do mar e suas montanhas.', fotos='floripa.png', idcidade=13)
]

# INSERINDO AS CLASSES DO VOO
classes_voo = [
    ClasseVoo(idclassevoo=1, nomeclassevoo='Economica', preco_classe=650.45),
    ClasseVoo(idclassevoo=2, nomeclassevoo='Economica Premium', preco_classe=895.90),
    ClasseVoo(idclassevoo=3, nomeclassevoo='Executiva', preco_classe=2115.20),
    ClasseVoo(idclassevoo=4, nomeclassevoo='Primeira Classe', preco_classe=10050.00)
]

# INSERINDO AS PASSAGENS
passagens = [
    Passagem(idpassagem=1, data_ida='2020-05-25 04:30', data_volta='2020-06-01 19:15', idorigem=1, iddestino=2, duracao='04:04', companhia_aerea='GOL', qtde_pessoas=2, idclassevoo=2),
    Passagem(idpassagem=2, data_ida='2020-06-01 10:00', data_volta='2020-06-08 20:30', idorigem=10, iddestino=1, duracao='01:10', companhia_aerea='GOL', qtde_pessoas=6, idclassevoo=4),
    Passagem(idpassagem=3, data_ida='2020-07-14 14:00', data_volta='2020-07-17 10:00', idorigem=13, iddestino=5, duracao='01:30', companhia_aerea='LATAM', qtde_pessoas=2, idclassevoo=2),
    Passagem(idpassagem=4, data_ida='2020-08-29 09:45', data_volta='2020-09-04 12:00', idorigem=3, iddestino=6, duracao='03:15', companhia_aerea='Azul', qtde_pessoas=3, idclassevoo=1),
    Passagem(idpassagem=5, data_ida='2020-09-15 14:30', data_volta='2020-09-22 17:45', idorigem=8, iddestino=7, duracao='02:45', companhia_aerea='LATAM', qtde_pessoas=4, idclassevoo=3),
    Passagem(idpassagem=6, data_ida='2020-10-05 08:00', data_volta='2020-10-12 10:30', idorigem=11, iddestino=8, duracao='02:00', companhia_aerea='GOL', qtde_pessoas=2, idclassevoo=2),
    Passagem(idpassagem=7, data_ida='2020-11-20 11:15', data_volta='2020-11-27 13:45', idorigem=4, iddestino=9, duracao='01:30', companhia_aerea='Azul', qtde_pessoas=1, idclassevoo=4),
    Passagem(idpassagem=8, data_ida='2020-12-10 15:30', data_volta='2020-12-17 18:00', idorigem=2, iddestino=3, duracao='02:15', companhia_aerea='GOL', qtde_pessoas=3, idclassevoo=1),
    Passagem(idpassagem=9, data_ida='2021-01-05 07:45', data_volta='2021-01-12 10:15', idorigem=6, iddestino=11, duracao='02:30', companhia_aerea='LATAM', qtde_pessoas=2, idclassevoo=2),
    Passagem(idpassagem=10, data_ida='2021-02-18 13:00', data_volta=None, idorigem=5, iddestino=12,duracao='03:00', companhia_aerea='Azul', qtde_pessoas=1, idclassevoo=3)
]

# INSERINDO OS HOTEIS
hoteis = [
    Hotel(idhotel=1, nome_hotel='Pousada do Porto', qtdehospedes=5, qtdequartos=2, idendereco=20),
    Hotel(idhotel=2, nome_hotel='Sky Serra Hotel', qtdehospedes=8, qtdequartos=3, idendereco=21),
    Hotel(idhotel=3, nome_hotel='WZ Hotel Jardins', qtdehospedes=2, qtdequartos=1, idendereco=22),
    Hotel(idhotel=4, nome_hotel='Copacabana Palace, A Belmond Hotel', qtdehospedes=6, qtdequartos=2, idendereco=23),
    Hotel(idhotel=5, nome_hotel='Hotel Centro Europeu', qtdehospedes=12, qtdequartos=4, idendereco=24),
    Hotel(idhotel=6, nome_hotel='Hotel Costa Mar', qtdehospedes=9, qtdequartos=3, idendereco=25),
    Hotel(idhotel=7, nome_hotel='Nacional Inn Torres', qtdehospedes=2, qtdequartos=2, idendereco=26),
    Hotel(idhotel=8, nome_hotel='Hotel Terra Brasil', qtdehospedes=1, qtdequartos=1, idendereco=27),
    Hotel(idhotel=9, nome_hotel='Hotel Refúgio', qtdehospedes=4, qtdequartos=2, idendereco=28),
    Hotel(idhotel=10, nome_hotel='Numar Hotel', qtdehospedes=8, qtdequartos=4, idendereco=29)
]

# INSERINDO AS PASSAGENS DOS USUARIOS
usuario_has_passagem = [
    UsuarioHasPassagem(cpf='12345676543', idpassagem=1, comentario='Ótima viagem, recomendo!'),
    UsuarioHasPassagem(cpf='3334445556', idpassagem=2, comentario='Serviço de bordo excelente.'),
    UsuarioHasPassagem(cpf='15142365890', idpassagem=3, comentario='Atrasos frequentes, não recomendo.'),
    UsuarioHasPassagem(cpf='23454366654', idpassagem=4, comentario='Viagem tranquila, gostei muito.'),
    UsuarioHasPassagem(cpf='44355688921', idpassagem=5, comentario='Ótimo atendimento da tripulação.'),
    UsuarioHasPassagem(cpf='15142365890', idpassagem=6, comentario='Bagagem extraviada, péssima experiência.'),
    UsuarioHasPassagem(cpf='78956432144', idpassagem=7, comentario='Voo cancelado sem aviso prévio, insatisfeito.'),
    UsuarioHasPassagem(cpf='21343255565', idpassagem=8, comentario='Serviço de entretenimento a bordo muito bom.'),
    UsuarioHasPassagem(cpf='32155547899', idpassagem=9, comentario='Assentos desconfortáveis, não recomendo.'),
    UsuarioHasPassagem(cpf='44355688921', idpassagem=10, comentario='Excelente serviço, vale a pena.')
]

#  INSERINDO AS HOSPEDAGENS
hospedagem = [
    Hospedagem(idhospedagem=1, idhotel=4, precos=826.00, entrada='2020-05-25', saida='2020-05-30'),
    Hospedagem(idhospedagem=2, idhotel=2, precos=1134.60, entrada='2020-06-02', saida='2020-06-07'),
    Hospedagem(idhospedagem=3, idhotel=3, precos=675.50, entrada='2020-07-15', saida='2020-07-18'),
    Hospedagem(idhospedagem=4, idhotel=4, precos=5355.20, entrada='2020-08-30', saida='2020-09-03'),
    Hospedagem(idhospedagem=5, idhotel=8, precos=8445.30, entrada='2020-09-16', saida='2020-09-20'),
    Hospedagem(idhospedagem=6, idhotel=6, precos=1458.15, entrada='2020-10-06', saida='2020-10-10'),
    Hospedagem(idhospedagem=7, idhotel=9, precos=2740.90, entrada='2020-11-21', saida='2020-11-25'),
    Hospedagem(idhospedagem=8, idhotel=1, precos=264.00, entrada='2020-12-11', saida='2020-12-15'),
    Hospedagem(idhospedagem=9, idhotel=10, precos=2118.00, entrada='2021-01-06', saida='2021-01-10'),
    Hospedagem(idhospedagem=10, idhotel=6, precos=3024.70, entrada='2021-02-19', saida='2021-02-23')
]

# INSERINDO AS HOSPEDAGENS DOS USUARIOS
usuario_has_hospedagem = [
    UsuarioHasHospedagem(cpf='12345676543', idhospedagem=1, comentario='Ótima estadia, hotel bem localizado.'),
    UsuarioHasHospedagem(cpf='3334445556', idhospedagem=2, comentario='Serviço de quarto excelente.'),
    UsuarioHasHospedagem(cpf='15142365890', idhospedagem=3, comentario='Hotel com vista incrível para o mar.'),
    UsuarioHasHospedagem(cpf='23454366654', idhospedagem=4, comentario='Excelente café da manhã.'),
    UsuarioHasHospedagem(cpf='44355688921', idhospedagem=5, comentario='Atendimento cordial, recomendo.'),
    UsuarioHasHospedagem(cpf='15142365890', idhospedagem=6, comentario='Piscina estava fechada, decepcionante.'),
    UsuarioHasHospedagem(cpf='78956432144', idhospedagem=7, comentario='Hotel bem cuidado, ótima experiência.'),
    UsuarioHasHospedagem(cpf='21343255565', idhospedagem=8, comentario='Quartos limpos e confortáveis.'),
    UsuarioHasHospedagem(cpf='32155547899', idhospedagem=9, comentario='Wi-Fi instável, precisa de melhorias.'),
    UsuarioHasHospedagem(cpf='44355688921', idhospedagem=10, comentario='Ótimo custo-benefício, voltaria com certeza.')
]


session.add_all(usuarios)
session.add_all(estados)
session.add_all(cidades)
session.add_all(enderecos)
session.add_all(origens)
session.add_all(destinos)
session.add_all(classes_voo)
session.add_all(passagens)
session.add_all(hoteis)
session.add_all(usuario_has_passagem)
session.add_all(hospedagem)
session.add_all(usuario_has_hospedagem)

session.commit()

# LER AS TABELAS

# lendo usuários
rusuarios = session.query(Usuario).all()
for usuario in rusuarios:
    print(usuario.cpf, usuario.nome, usuario.email, usuario.senha)

# lendo estados
restados = session.query(Estado).all()
for estado in restados:
    print(estado.idestado, estado.nome_estado)

# lendo cidades
rcidades = session.query(Cidade).all()
for cidade in rcidades:
    print(cidade.idcidade, cidade.nome_cidade, cidade.idestado)

# lendo enderecos
renderecos = session.query(Endereco).all()
for endereco in renderecos:
    print(endereco.idendereco, endereco.rua, endereco.numero, endereco.idcidade)

# lendo origens
rorigens = session.query(Origem).all()
for origem in rorigens:
    print(origem.idorigem, origem.idendereco)

# lendo destinos
rdestinos = session.query(Destinos).all()
for destino in rdestinos:
    print(destino.iddestino, destino.descricao, destino.fotos, destino.idcidade)

# lendo classes_voo
rclasses_voo = session.query(ClasseVoo).all()
for classe in rclasses_voo:
    print(classe.idclassevoo, classe.nomeclassevoo, classe.preco_classe)

# lendo passagens
rpassagens = session.query(Passagem).all()
for passagem in rpassagens:
    print(passagem.idpassagem, passagem.data_ida, passagem.data_volta, passagem.idorigem, passagem.iddestino, passagem.duracao, passagem.companhia_aerea, passagem.qtde_pessoas, passagem.idclassevoo)

# lendo hoteis
rhoteis = session.query(Hotel).all()
for hotel in rhoteis:
    print(hotel.idhotel, hotel.nome_hotel, hotel.qtdehospedes, hotel.qtdequartos, hotel.idendereco)

# lendo usuario_has_passagem
rusuario_has_passagem = session.query(UsuarioHasPassagem).all()
for usuario in rusuario_has_passagem:
    print(usuario.cpf, usuario.idpassagem, usuario.comentario)

# lendo hospedagem
rhospedagem = session.query(Hospedagem).all()
for hospedagem in rhospedagem:
    print(hospedagem.idhospedagem, hospedagem.idhotel, hospedagem.precos, hospedagem.entrada, hospedagem.saida)

# lendo usuario_has_hospedagem
rusuario_has_hospedagem = session.query(UsuarioHasHospedagem).all()
for usuario in rusuario_has_hospedagem:
    print(usuario.cpf, usuario.idhospedagem, usuario.comentario)

session.commit()

# ATUALIZAR AS TABELAS

session.query(Usuario).filter(Usuario.cpf == "23454366654").update( { "nome" : "Luciana Passos"})
session.query(Endereco).filter(Endereco.idendereco == 14).update( { "rua" : "Rua Ipe"})
session.query(Hospedagem).filter(Hospedagem.idhospedagem == 3).update( { "precos" : "1000"})
session.query(Hotel).filter(Hotel.idhotel == 1).update( { "qtdequartos" : "1"})

session.commit()

# EXCLUIR DADOS DAS TABELAS

session.query(Usuario).filter(Usuario.cpf == "19027198913").delete()
session.query(UsuarioHasHospedagem).filter(UsuarioHasHospedagem.idhospedagem == 1).delete()
session.query(Hospedagem).filter(Hospedagem.idhospedagem == 1).delete()
session.query(Endereco).filter(Endereco.idendereco == 30).delete()

session.close() 