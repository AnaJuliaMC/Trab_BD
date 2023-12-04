import psycopg2
# from agenciaviagem import get_conexao_postgres

def get_conexao_postgres(banco_de_dados: str = "agenciaviagem", usuario: str = "defendii", senha: str = "GowE3Q6AcDny", host: str = "ep-cool-mouse-71322146.us-east-2.aws.neon.tech", porta: int = 5432):
    conn = psycopg2.connect(
    host = host,
    database = banco_de_dados,
    user = usuario,
    password = senha,
    port = porta
    )
    return conn

def criar_tabela_usuario():
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE usuario(
                cpf VARCHAR(11) not null,
                nome VARCHAR(50) not null,
                email VARCHAR(50)not null,
                senha VARCHAR(15) not null,
                PRIMARY KEY(cpf));
                """)
        
        usuario = [
            ('12345676543', 'Ana Silva', 'anasilva@gmail.com', 'anasilva123'),
            ('3334445556', 'Juliana Rocha', 'jurocha@gmail.com', 'amogatos123'),
            ('1234567891', 'Larissa Ramos', 'larilinda@gmail.com', 'larizinhaah'),
            ('5556667778', 'Eduardo Pena', 'edupena@gmail.com', 'edupena1'),
            ('11587806988', 'Hiago Gimenez', 'giagimenez1@gmail.com', 'hiago88'),
            ('15142365890', 'João Bühler', 'ruivinho1@gmail.com', 'ruivodamene'),
            ('19892345726', 'Maria Menezes', 'mariam123@gmail.com', '210492'),
            ('83561809264', 'Marcela Viera', 'vierama@gmail.com', 'ferrari'),
            ('19027198913', 'Ana Almeida', 'almeidaana13@gmail.com', 'taylorswift13'),
            ('11122233387', 'Maisa Silva', 'maisasilvaofc@gmail.com', 'silvamah1'),
            ('29876587621', 'Flavia Reitz', 'flaviareitz@gmail.com', 'farc78'),
            ('56789123455', 'Luana Cardoso', 'luaninha@gmail.com', 'luluzinha'),
            ('45321168876', 'Maria Julia Rodrigues', 'jujumaria@gmail.com', 'senhadificil11'),
            ('23454314522', 'João Augusto Costa', 'jaugust@gmail.com', 'viajante1'),
            ('78956432144', 'Matheus Lima', 'lmatt@gmail.com', 'soulindo1'),
            ('21343255565', 'Larissa Manoela', 'larimanu@gmail.com', 'laricell11'),
            ('32155547899', 'Karina Costa', 'familiaviajante@gmail.com', 'viajante2'),
            ('44355688921', 'Virginia Fonseca', 'fonsecav@gmail.com', 'maedasmarias'),
            ('15678955567', 'Luiz Marcio Nogueira', 'marcinho@gmail.com', 'luizinhom12'),
            ('23454366654', 'Luciah Sophie Pereira', 'luciacomh@gmail.com', 'luciahsophie')]

        cursor.executemany("""
        INSERT INTO usuario (cpf, nome, email, senha)
        VALUES (%s, %s, %s, %s);
        """, (usuario))

        conexao.commit()

        cursor.close()
        conexao.close()

        print("Tabela usuario criada e populada com sucesso!")
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao criar a tabela usuario: {erro}")


def criar_tabela_estado():
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE estado(
                idestado INT NOT NULL,
                nome_estado VARCHAR(100) NOT NULL,
                PRIMARY KEY(idestado)
                );
                """)
        
        estado = [
            (1, 'Rio de Janeiro'),
            (2, 'Rio Grande do Sul'),
            (3, 'Maranhão'),
            (4, 'Paraná'),
            (5, 'São Paulo'),
            (6, 'Bahia'),
            (7, 'Mato Grosso do Sul'),
            (8, 'Tocantins'),
            (9, 'Paraíba'),
            (10, 'Alagoas'),
            (11, 'Santa Catarina')
            ]
        
        cursor.executemany("""
            INSERT INTO estado (idestado, nome_estado)
            VALUES (%s, %s);
            """, (estado))
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print("Tabela estado criada e populada com sucesso!")
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao criar a tabela estado: {erro}")

def criar_tabela_cidade():
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE cidade(
                idcidade INT NOT NULL,
                nome_cidade VARCHAR(100) NOT NULL,
                idestado INT NOT NULL,
                PRIMARY KEY(idcidade),
                FOREIGN KEY(idestado) REFERENCES estado(idestado)
                );
                """)
        
        cidade = [
            (1, 'Rio de Janeiro', 1),
            (2, 'Gramado', 2),
            (3, 'Barreirinhas', 3),
            (4, 'Curitiba', 4),
            (5, 'São Paulo', 5),
            (6, 'Foz do Iguaçu', 4),
            (7, 'Porto Seguro', 6),
            (8, 'Bonito', 7),
            (9, 'Mateiros', 8),
            (10, 'Campos do Jordão', 5),
            (11, 'João Pessoa', 9),
            (12, 'Maceió', 10),
            (13, 'Florianópolis', 11),
            (14, 'Maringá', 4)
            ]
        
        cursor.executemany("""
        INSERT INTO cidade (idcidade, nome_cidade, idestado)
        VALUES (%s, %s, %s);
        """, (cidade))

        conexao.commit()

        cursor.close()
        conexao.close()

        print("Tabela cidade criada e populada com sucesso!")
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao criar a tabela cidade: {erro}")

def criar_tabela_endereco():
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE endereco(
                idendereco INT NOT NULL,
                rua VARCHAR(50) NOT NULL,
                numero VARCHAR(6) NOT NULL,
                idcidade INT NOT NULL,
                PRIMARY KEY(idendereco),
                FOREIGN KEY(idcidade) REFERENCES cidade(idcidade)
                );
                """)
        
        endereco = [
            (1, 'Rua das Flores', '311', 12),
            (2, 'Rua Maringa', '21', 14),
            (3, 'Rua Girassol', '01', 1),
            (4, 'Rua Goias', '411', 8),
            (5, 'Rua São Paulo', '2012', 5),
            (6, 'Rua Pato Branco', '267', 14),
            (7, 'Rua Evermore', '13', 10),
            (8, 'Rua Beltrão', '127', 9),
            (9, 'Rua das Araras', '31', 8),
            (10, 'Rua da Fama', '189', 5),
            (11, 'Rua Amores', '25', 3),
            (12, 'Avenida Principal', '890', 6),
            (13, 'Rua das Casinhas', '900', 7),
            (14, 'Rua Girassol', '23', 13),
            (15, 'Avenida Joao Pessoa', '77', 12),
            (16, 'Rua da Fama', '155', 1),
            (17, 'Avenida dos Empresarios', '89', 5),
            (18, 'Rua Cianorte', '601', 2),
            (19, 'Avenida da Paz', '311', 11),
            (20, 'R. Anacleto de Carvalho', '475', 3),
            (21, 'R. Tirol', '149', 2),
            (22, 'Av. Rebouças', '955', 5),
            (23, 'Av. Atlântica', '1702', 1),
            (24, 'Praça Gen. Osório', '61', 4),
            (25, 'R. Machado Lemos', '433', 12),
            (26, 'R. Mariano Torres', '976', 4),
            (27, 'R. do Cajueiro', '5', 7),
            (28, 'R. Nossa Sra. da Penha', '366', 8),
            (29, 'Av. Gov. Argemiro de Figueiredo', '3197', 11),
            (30, 'Avenida Costa e Silva', '154', 6)
            ]
        
        cursor.executemany("""
            INSERT INTO endereco (idendereco, rua, numero, idcidade)
            VALUES (%s, %s, %s, %s);
            """, (endereco))
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print("Tabela endereco criada e populada com sucesso!")
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao criar a tabela endereco: {erro}")

def criar_tabela_destinos():
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE destinos(
                iddestino int not NULL,
                descriçao VARCHAR(500) not null,
                fotos VARCHAR(20)not NULL,
                idcidade INT NOT NULL,
                PRIMARY KEY (iddestino),
                FOREIGN KEY(idcidade) REFERENCES cidade(idcidade));
                """)
        
        destinos = [ 
            (1, 'Existem vários motivos que fazem do Rio um dos cartões postais brasileiros mais conhecidos em todo o mundo, e suas belas praias com certeza são um deles! Copacabana, Ipanema, Leblon, Praia do Arpoador e muitas outras contornam a cidade maravilhosa como a moldura perfeita','riodejaneiro123.png', 1),
            (2, 'Gramado é a principal cidade da Serra Gaúcha e sem dúvidas é um dos melhores destinos turísticos do país. Romântica, charmosa, cheia de cultura, belas paisagens, atrações e ótima culinária, Gramado é capaz de agradar a todos e sempre oferece novas opções.', 'gramado321.png', 2),
            (3, 'Mais uma vez a beleza natural aparecendo na lista das atrações surpreendentes do Nordeste brasileiro. Com lindas lagoas, dunas brancas e um ecossistema único, aqui é possível conferir de perto um dos mais belos conjunto de paisagens do país.', 'lencoismaa.png', 3),
            (4, 'A cidade de Curitiba, capital do estado do Paraná, é conhecida pelo cuidado com o planejamento urbano, belas áreas verdes e um transporte público de qualidade. A fama não é para menos. Curitiba realmente oferece um excelente padrão de vida para os moradores.', 'curitiba2.png', 4),
            (5, 'São Paulo, centro financeiro do Brasil, está entre as cidades mais populosas do mundo, com diversas instituições culturais e uma rica tradição arquitetônica.', 'saopaulo.png', 5),
            (6, 'Foz do Iguaçu é uma cidade turísticas que fica no sul do Brasil, conhecida pelas Cataratas do Iguaçu, por fazer fronteira com Paraguai e Argentina, pelos hotéis e pousadas e seus ambientes familiares, e por estar se tornando um polo de parques temáticos no Brasil.', 'cataratasfoz.png', 6),
            (7, 'Porto Seguro é um dos destinos de praia preferidos no Brasil, em virtude de suas belíssimas praias, da farta rede hoteleira e por ser o destino mais próximo do Nordeste para quem mora no Sul e Sudeste do país.', 'portoseguro.png', 7),
            (8, 'Bonito é considerado um dos melhores destinos de ecoturismo do Brasil, por causa da beleza de seus atrativos, mas também da forma rigorosa como são preservados.', 'bonito.png', 8),
            (9, 'Mateiros é o verdadeiro paraíso em meio ao cerrado brasileiro. Lá você encontrará diversas atividades ao ar livre que te encantarão.', 'parquejalapao.png', 9),
            (10, 'Campos do Jordão é um dos destinos queridinhos do Brasil, ótima opção o ano inteiro, principalmente no inverno! É um lugar cercado pelo charme das montanhas, influenciado pela cultura europeia, cheio de restaurantes e atividades para pessoas de todas as idades.', 'camposjordao.png', 10),
            (11, 'Viajar para João Pessoa é encontrar praias maravilhosas e um povo muito receptivo e orgulhoso de sua região. Aposte na Paraíba, e você não vai se arrepender.', 'joaopessoa1.png', 11),
            (12, 'Maceió, tem um jeitinho de cidade do interior e ritmo menos acelerado do que outras capitais brasileiras, e esse é um de seus grandes charmes. Os turistas que a visitam contam com restaurantes de qualidade, bons hotéis, além de ótimas praias e diversidade de passeios.', 'maceio.png', 12),
            (13, 'Conhecida como Ilha da Magia e carinhosamente chamada de Floripa, cada pedacinho de Florianópolis tem uma característica distinta, sendo sempre sua principal atração a Natureza, especialmente através do mar e suas montanhas.', 'floripa.png', 13)
            ]
        
        cursor.executemany("""
            INSERT INTO destinos (iddestino, descriçao, fotos, idcidade)
            VALUES (%s, %s, %s, %s);
            """, (destinos))
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print("Tabela destinos criada e populada com sucesso!")
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao criar a tabela destinos: {erro}")
 
def criar_tabela_origem():
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE origem(
                idorigem INT NOT NULL,
                idendereco INT NOT NULL,
                PRIMARY KEY(idorigem),
                FOREIGN KEY(idendereco) REFERENCES endereco(idendereco)
                );
                """)
        
        origem = [ 
            (1, 19),
            (2, 17),
            (3, 16),
            (4, 15), 
            (5, 14),
            (6, 13),
            (7, 12),
            (8, 10),
            (10, 9),
            (11, 8),
            (12, 6), 
            (13, 4),
            (14, 3),
            (15, 1)
            ]
        
        cursor.executemany("""
            INSERT INTO origem (idorigem, idendereco)
            VALUES (%s, %s);
            """, (origem))
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print("Tabela origem criada e populada com sucesso!")
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao criar a tabela origem: {erro}")
 
def criar_tabela_classevoo():
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE classevoo(
                idclassevoo INT NOT NULL,
                nomeclassevoo VARCHAR(30) NOT NULL,
                preco_classe FLOAT,
                PRIMARY KEY (idclassevoo)
                );
                """)
        
        classevoo = [
            (1, 'Economica', 650.45),
            (2, 'Economica Premium', 895.90),
            (3, 'Executiva', 2115.20),
            (4, 'Primeira Classe', 10050)
            ]
        
        cursor.executemany("""
            INSERT INTO classevoo (idclassevoo, nomeclassevoo, preco_classe)
            VALUES (%s, %s, %s);
            """, (classevoo))
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print("Tabela classe_voo criada e populada com sucesso!")
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao criar a tabela classe_voo: {erro}")

def criar_tabela_passagem():
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE passagem(
                idpassagem INT not null, 
                data_ida TIMESTAMP not null,
                data_volta TIMESTAMP, 
                idorigem INT not null,
                iddestino INT not null,
                duração TIME not null,
                companhia_aerea VARCHAR(10) NOT NULL,
                qtde_pessoas INT NOT NULL,
                idclassevoo INT not NULL,
                PRIMARY key(idpassagem),
                FOREIGN KEY(iddestino) REFERENCES destinos(iddestino),
                FOREIGN KEY(idorigem) REFERENCES origem(idorigem),
                FOREIGN KEY(idclassevoo) REFERENCES classevoo (idclassevoo)
                );
                """) 
        
        passagem = [
            (1, '2020-05-25 04:30', '2020-06-01 19:15', 1, 2, '04:04', 'GOL' ,2, 2),
            (2, '2020-06-01 10:00', '2020-06-08 20:30', 10, 1, '01:10', 'GOL', 6, 4),
            (3, '2020-07-14 14:00', '2020-07-17 10:00', 13, 5, '01:30', 'LATAM', 2, 2),
            (4, '2020-08-29 09:45', '2020-09-04 12:00', 3, 6, '03:15', 'Azul', 3, 1),
            (5, '2020-09-15 14:30', '2020-09-22 17:45', 8, 7, '02:45', 'LATAM', 4, 3),
            (6, '2020-10-05 08:00', '2020-10-12 10:30', 11, 8, '02:00', 'GOL', 2, 2),
            (7, '2020-11-20 11:15', '2020-11-27 13:45', 4, 9, '01:30', 'Azul', 1, 4),
            (8, '2020-12-10 15:30', '2020-12-17 18:00', 2, 3, '02:15', 'GOL', 3, 1),
            (9, '2021-01-05 07:45', '2021-01-12 10:15', 6, 11, '02:30', 'LATAM', 2, 2),
            (10, '2021-02-18 13:00', NULL, 5, 12, '03:00', 'Azul', 1, 3)
            ]
        
        cursor.executemany("""
            INSERT INTO passagem (idpassagem, data_ida, data_volta, idorigem, iddestino, duração, companhia_aerea, qtde_pessoas, idclassevoo)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
            """, (passagem))
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print("Tabela passagem criada e populada com sucesso!")
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao criar a tabela passagem: {erro}")
 
def criar_tabela_hotel():
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE hotel(
                idhotel INT NOT NULL,
                nome_hotel VARCHAR(50),
                qtdehospedes INT NOT NULL,
                qtdequartos INT NOT NULL,
                idendereco INT NOT NULL,
                PRIMARY KEY(idhotel),
                FOREIGN KEY(idendereco) REFERENCES endereco(idendereco)
                );
                """) 
        
        hotel = [ 
            (1, 'Pousada do Porto', 5, 2, 20),
            (2, 'Sky Serra Hotel', 8, 3, 21),
            (3, 'WZ Hotel Jardins', 2, 1, 22),
            (4, 'Copacabana Palace, A Belmond Hotel', 6, 2, 23),
            (5, 'Hotel Centro Europeu', 12, 4, 24),
            (6, 'Hotel Costa Mar', 9, 3, 25),
            (7, 'Nacional Inn Torres', 2, 2, 26),
            (8, 'Hotel Terra Brasil', 1, 1, 27),
            (9, 'Hotel Refúgio', 4, 2, 28),
            (10, 'Numar Hotel', 8, 4, 29)
            ]
        
        cursor.executemany("""
            INSERT INTO hotel (idhotel, nome_hotel, qtdehospedes, qtdequartos, idendereco)
            VALUES (%s, %s, %s, %s, %s);
            """, (hotel))
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print("Tabela hotel criada e populada com sucesso!")
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao criar a tabela hotel: {erro}")
 
def criar_tabela_hospedagem():
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE hospedagem(
                idhospedagem INT NOT NULL,
                idhotel INT NOT NULL,
                precos FLOAT not null,
                entrada DATE not null,
                saida DATE not null,
                PRIMARY KEY(idhospedagem),
                FOREIGN KEY(idhotel) REFERENCES hotel(idhotel));
                """) 
        
        hospedagem = [ 
            (1, 4, 826.00, '2020-05-25', '2020-05-30'),
            (2, 2, 1134.60, '2020-06-02', '2020-06-07'),
            (3, 3, 675.50, '2020-07-15', '2020-07-18'),
            (4, 4, 5355.20, '2020-08-30', '2020-09-03'),
            (5, 8, 8445.30, '2020-09-16', '2020-09-20'),
            (6, 6, 1458.15, '2020-10-06', '2020-10-10'),
            (7, 9, 2740.90, '2020-11-21', '2020-11-25'),
            (8, 1, 264.00, '2020-12-11', '2020-12-15'),
            (9, 10, 2118.00, '2021-01-06', '2021-01-10'),
            (10, 6, 3024.70, '2021-02-19', '2021-02-23')
            ]
        
        cursor.executemany("""
            INSERT INTO hospedagem (idhospedagem, idhotel, precos, entrada, saida)
            VALUES (%s, %s, %s, %s, %s);
            """, (hospedagem))
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print("Tabela hospedagem criada e populada com sucesso!")
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao criar a tabela hospedagem: {erro}")
            
def criar_tabela_usuario_has_hospedagem():
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE usuario_has_hospedagem(
                cpf VARCHAR(11) NOT NULL,
                idhospedagem INT NOT NULL,
                comentario VARCHAR(500) NOT NULL,
                FOREIGN KEY (cpf) REFERENCES usuario(cpf),
                FOREIGN KEY (idhospedagem) REFERENCES hospedagem(idhospedagem)
                );
                """) 
        
        usuario_has_hospedagem = [
            ('12345676543', 1, 'Ótima estadia, hotel bem localizado.'),
            ('3334445556', 2, 'Serviço de quarto excelente.'),
            ('15142365890', 3, 'Hotel com vista incrível para o mar.'),
            ('23454366654', 4, 'Excelente café da manhã.'),
            ('44355688921', 5, 'Atendimento cordial, recomendo.'),
            ('15142365890', 6, 'Piscina estava fechada, decepcionante.'),
            ('78956432144', 7, 'Hotel bem cuidado, ótima experiência.'),
            ('21343255565', 8, 'Quartos limpos e confortáveis.'),
            ('32155547899', 9, 'Wi-Fi instável, precisa de melhorias.'),
            ('44355688921', 10, 'Ótimo custo-benefício, voltaria com certeza.')
        ]
        
        cursor.executemany("""
            INSERT INTO usuario_has_hospedagem (cpf, idhospedagem, comentario)
            VALUES (%s, %s, %s);
            """, (usuario_has_hospedagem))
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print("Tabela usuario_has_hospedagem criada e populada com sucesso!")
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao criar a tabela usuario_has_hospedagem: {erro}")

def criar_tabela_usuario_has_passagem():
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE usuario_has_passagem(
                cpf VARCHAR(11) NOT NULL,
                idpassagem INT NOT NULL,
                comentario VARCHAR(500) NOT NULL,
                FOREIGN KEY (cpf) REFERENCES usuario(cpf),
                FOREIGN KEY (idpassagem) REFERENCES passagem(idpassagem)
                );
                """) 
        
        usuario_has_passagem = [
            ('12345676543', 1, 'Ótima viagem, recomendo!'),
            ('3334445556', 2, 'Serviço de bordo excelente.'),
            ('15142365890', 3, 'Atrasos frequentes, não recomendo.'),
            ('23454366654', 4, 'Viagem tranquila, gostei muito.'),
            ('44355688921', 5, 'Ótimo atendimento da tripulação.'),
            ('15142365890', 6, 'Bagagem extraviada, péssima experiência.'),
            ('78956432144', 7, 'Voo cancelado sem aviso prévio, insatisfeito.'),
            ('21343255565', 8, 'Serviço de entretenimento a bordo muito bom.'),
            ('32155547899', 9, 'Assentos desconfortáveis, não recomendo.'),
            ('44355688921', 10, 'Excelente serviço, vale a pena.')
        ]

        cursor.executemany("""
            INSERT INTO usuario_has_passagem (cpf, idpassagem, comentario)
            VALUES (%s, %s, %s);
            """, (usuario_has_passagem))
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print("Tabela usuario_has_passagem criada e populada com sucesso!")
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao criar a tabela usuario_has_passagem: {erro}")

# create
def create_usuario(cpf, nome, email, senha):
    print(f"(create_usuario) Criando o usuario {nome}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO usuario (cpf, nome, email, senha)
        VALUES (%s, %s, %s, %s);
        """, (cpf, nome, email, senha))

        conexao.commit()

        cursor.close()
        conexao.close()

        print(f'Usuario com nome {nome}, e cpf {cpf} criado com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao criar o usuario: {erro}")


def create_estado(idestado, nome_estado):
    print(f"(create_estado) Criando o estado {nome_estado}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO estado (idestado, nome_estado)
            VALUES (%s, %s);
            """, (idestado, nome_estado))
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print(f"Estado {nome_estado} e id {idestado} criado com sucesso!")
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao criar o estado: {erro}")

def create_cidade(idcidade, nome_cidade, idestado):
    print(f"(create_cidade) Criando a cidade {nome_cidade}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO cidade (idcidade, nome_cidade, idestado)
        VALUES (%s, %s, %s);
        """, (idcidade, nome_cidade, idestado))

        conexao.commit()

        cursor.close()
        conexao.close()

        print(f'Cidade com nome {nome_cidade}, e id {idcidade} criada com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao criar a cidade: {erro}")

def create_endereco(idendereco, rua, numero, idcidade):
    print(f"(create_endereco) Criando o endereço {idendereco}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO endereco (idendereco, rua, numero, idcidade)
            VALUES (%s, %s, %s, %s);
            """, (idendereco, rua, numero, idcidade))
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print(f'Endereço com id {idendereco}, e rua {rua} criado com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao criar o endereco: {erro}")

def create_destinos(iddestino, descriçao, fotos, idcidade):
    print(f"(create_destinos) Criando o destino {iddestino}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO destinos (iddestino, descriçao, fotos, idcidade)
            VALUES (%s, %s, %s, %s);
            """, (iddestino, descriçao, fotos, idcidade))
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print(f'Destino com id {iddestino}, e cidade {idcidade} criado com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao criar o destino: {erro}")
 
def create_origem(idorigem, idendereco):
    print(f"(create_origem) Criando a origem {idorigem}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO origem (idorigem, idendereco)
            VALUES (%s, %s);
            """, (idorigem, idendereco))
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print(f'Origem com id {idorigem}, e endereco {idendereco} criado com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao criar a origem: {erro}")
 
def create_classevoo(idclassevoo, nomeclassevoo, preco_classe):
    print(f"(create_classevoo) Criando a classe {idclassevoo}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO classevoo (idclassevoo, nomeclassevoo, preco_classe)
            VALUES (%s, %s, %s);
            """, (idclassevoo, nomeclassevoo, preco_classe))
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print(f'Classe {nomeclassevoo}, e id {idclassevoo} criada com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao criar a classe do voo: {erro}")

def create_passagem(idpassagem, data_ida, data_volta, idorigem, iddestino, duração, companhia_aerea, qtde_pessoas, idclassevoo):
    print(f"(create_passagem) Criando a passagem {idpassagem}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO passagem (idpassagem, data_ida, data_volta, idorigem, iddestino, duração, companhia_aerea, qtde_pessoas, idclassevoo)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
            """, (idpassagem, data_ida, data_volta, idorigem, iddestino, duração, companhia_aerea, qtde_pessoas, idclassevoo)) 
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print(f'Passagem com id {idpassagem} criada com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao criar a passagem: {erro}")
 
def create_hotel(idhotel, nome_hotel, qtdehospedes, qtdequartos, idendereco):
    print(f"(create_hotel) Criando o hotel {idhotel}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO hotel (idhotel, nome_hotel, qtdehospedes, qtdequartos, idendereco)
            VALUES (%s, %s, %s, %s, %s);
            """, (idhotel, nome_hotel, qtdehospedes, qtdequartos, idendereco)) 
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print(f'Hotel {nome_hotel}, e id {idhotel} criado com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao criar o hotel: {erro}")
 
def create_hospedagem(idhospedagem, idhotel, precos, entrada, saida):
    print(f"(create_hospagem) Criando a hospedagem {idhospedagem}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO hospedagem (idhospedagem, idhotel, precos, entrada, saida)
            VALUES (%s, %s, %s, %s, %s);
            """, (idhospedagem, idhotel, precos, entrada, saida)) 
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print(f'Hosdagem com id {idhospedagem}, e hotel {idhotel} criada com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao criar a hospedagem: {erro}")
            
def create_usuario_has_hospedagem(cpf, idhospedagem, comentario):
    print(f"(create_usuario_has_hospedagem) Criando a hospedagem do usuario {cpf}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO usuario_has_hospedagem (cpf, idhospedagem, comentario)
            VALUES (%s, %s, %s);
            """, (cpf, idhospedagem, comentario)) 
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print(f'Usuario com cpf {cpf}, e id de hospedagem {idhospedagem} criado com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao criar a hospedagem do usuario: {erro}")

def create_usuario_has_passagem(cpf, idpassagem, comentario):
    print(f"(create_usuario_has_passagem) Criando a passagem do usuario {cpf}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO usuario_has_passagem (cpf, idpassagem, comentario)
            VALUES (%s, %s, %s);
            """, (cpf, idpassagem, comentario)) 
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print(f'Usuario com cpf {cpf}, e id de passagem {idpassagem} criado com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao criar a passagem do usuario: {erro}")

# read de um elemento

def read_usuario(cpf):
    print(f"(read_usuario) Buscando o usuario {cpf}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM usuario WHERE cpf = %s;
        """, (cpf,))

        usuarios = cursor.fetchall()

        for usu in usuarios:
            print(usu)

        cursor.close()
        conexao.close()

        return usuarios
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao buscar o usuario: {erro}")

def read_estado(idestado, nome_estado):
    print(f"(read_estado) Buscando o estado {nome_estado}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM estado WHERE idestado = %s;
        """, (idestado,))

        estados = cursor.fetchall()

        for estad in estados:
            print(estad)

        cursor.close()
        conexao.close()

        return estados
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao buscar os estados: {erro}")


def read_cidade(idcidade, nome_cidade):
    print(f"(read_cidade) Buscando a cidade {nome_cidade}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM cidade WHERE idcidade = %s;
        """, (idcidade,))

        cidades = cursor.fetchall()

        for cidad in cidades:
            print(cidad)

        cursor.close()
        conexao.close()

        return cidades
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao buscar as cidades: {erro}")

def read_endereco(idendereco):
    print(f"(read_endereco) Buscando o endereço {idendereco}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM endereco WHERE idendereco = %s;
        """, (idendereco,))
        
        enderecos = cursor.fetchall()

        for end in enderecos:
            print(end)

        cursor.close()
        conexao.close()

        return enderecos
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao buscar os enderecos: {erro}")

def read_destinos(iddestino):
    print(f"(read_destinos) Buscando o destino {iddestino}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM destinos WHERE iddestino = %s;
        """, (iddestino,))
        
        destinoss = cursor.fetchall()

        for destino in destinoss:
            print(destino)

        cursor.close()
        conexao.close()

        return destinoss
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao buscar os destinos: {erro}")
 
def read_origem(idorigem):
    print(f"(read_origem) Buscando a origem {idorigem}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM origem WHERE idorigem = %s;
        """, (idorigem,))
        
        origens = cursor.fetchall()

        for orig in origens:
            print(orig)

        cursor.close()
        conexao.close()

        return origens
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao buscar as origens: {erro}")
 
def read_classevoo(idclassevoo):
    print(f"(read_classevoo) Buscando a classe {idclassevoo}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
                SELECT * FROM classevoo WHERE idclassevoo = %s;
            """, (idclassevoo,))
        
        classes = cursor.fetchall()

        for classe in classes:
            print(classe)

        cursor.close()
        conexao.close()

        return classes
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao buscar as classes: {erro}")

def read_passagem(idpassagem):
    print(f"(read_passagem) Buscando a passagem {idpassagem}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM passagem WHERE idpassagem = %s;
        """, (idpassagem,))
        
        passagens = cursor.fetchall()

        for pas in passagens:
            print(pas)

        cursor.close()
        conexao.close()

        return passagens
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao buscar as passagens: {erro}")
 
def read_hotel(idhotel):
    print(f"(read_hotel) Buscando o hotel {idhotel}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM hotel WHERE idhotel = %s;
        """, (idhotel,)) 
        
        hoteis = cursor.fetchall()

        for hote in hoteis:
            print(hote)

        cursor.close()
        conexao.close()

        return hoteis
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao buscar os hoteis: {erro}")
 
def read_hospedagem(idhospedagem):
    print(f"(read_hospagem) Buscando a hospedagem {idhospedagem}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM hospedagem WHERE idhospedagem = %s;
        """, (idhospedagem,)) 
        
        hospedagens = cursor.fetchall()

        for hosp in hospedagens:
            print(hosp)

        cursor.close()
        conexao.close()

        return hospedagens
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao buscar as hospedagens: {erro}")

            
def read_usuario_has_hospedagem(cpf):
    print(f"(read_usuario_has_hospagem) Buscando a hospedagem do usuario {cpf}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM usuario_has_hospedagem WHERE cpf = %s;
        """, (cpf,))

        usu_has_hosps = cursor.fetchall()

        for usu_hosp in usu_has_hosps:
            print(usu_hosp)

        cursor.close()
        conexao.close()

        return usu_has_hosps
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao buscar as hospedagens dos usuarios: {erro}")

def read_usuario_has_passagem(cpf):
    print(f"(read_usuario_has_passagem) Buscando a passagem do usuario {cpf}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM usuario_has_passagem WHERE nome = %s;
        """, (cpf,))
        
        usu_has_pas = cursor.fetchall()

        for usu_pas in usu_has_pas:
            print(usu_pas)

        cursor.close()
        conexao.close()

        return usu_has_pas
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao buscar as passagens dos usuarios: {erro}")

# read all

def read_all_usuario():
    print(f"(read_all_usuario) Buscando todos usuarios...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM usuario;
        """)

        usuarios = cursor.fetchall()

        for usu in usuarios:
            print(usu)

        cursor.close()
        conexao.close()

        return usuarios
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao buscar os usuarios: {erro}")

def read_all_estado():
    print(f"(read_all_estado) Buscando todos estados...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM estado;
        """)

        estados = cursor.fetchall()

        for estad in estados:
            print(estad)

        cursor.close()
        conexao.close()

        return estados
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao buscar os estados: {erro}")


def read_all_cidade():
    print(f"(read_all_cidade) Buscando todas cidades...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM cidade;
        """)

        cidades = cursor.fetchall()

        for cidad in cidades:
            print(cidad)

        cursor.close()
        conexao.close()

        return cidades
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao buscar as cidades: {erro}")

def read_all_endereco():
    print(f"(read_all_endereco) Buscando todos endereços...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM endereco;
        """)
        
        enderecos = cursor.fetchall()

        for end in enderecos:
            print(end)

        cursor.close()
        conexao.close()

        return enderecos
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao buscar os enderecos: {erro}")

def read_all_destinos():
    print(f"(read_all_destinos) Buscando todos destinos...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM destinos;
        """)
        
        destinoss = cursor.fetchall()

        for destino in destinoss:
            print(destino)

        cursor.close()
        conexao.close()

        return destinoss
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao buscar os destinos: {erro}")
 
def read_all_origem():
    print(f"(read_all_origem) Buscando todas origens...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM origem;
        """)
        
        origens = cursor.fetchall()

        for orig in origens:
            print(orig)

        cursor.close()
        conexao.close()

        return origens
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao buscar as origens: {erro}")
 
def read_all_classevoo():
    print(f"(read_all_classevoo) Buscando todas classes...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
                SELECT * FROM classevoo;
            """)
        
        classes = cursor.fetchall()

        for classe in classes:
            print(classe)

        cursor.close()
        conexao.close()

        return classes
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao buscar as classes: {erro}")

def read_all_passagem():
    print(f"(read_all_passagem) Buscando todas passagens...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM passagem;
        """)
        
        passagens = cursor.fetchall()

        for pas in passagens:
            print(pas)

        cursor.close()
        conexao.close()

        return passagens
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao buscar as passagens: {erro}")
 
def read_all_hotel():
    print(f"(read_all_hotel) Buscando todos hoteis...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM hotel;
        """) 
        
        hoteis = cursor.fetchall()

        for hote in hoteis:
            print(hote)

        cursor.close()
        conexao.close()

        return hoteis
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao buscar os hoteis: {erro}")
 
def read_all_hospedagem():
    print(f"(read_all_hospagem) Buscando todas hospedagens...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM hospedagem;
        """) 
        
        hospedagens = cursor.fetchall()

        for hosp in hospedagens:
            print(hosp)

        cursor.close()
        conexao.close()

        return hospedagens
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao buscar as hospedagens: {erro}")

            
def read_all_usuario_has_hospedagem():
    print(f"(read_all_usuario_has_hospagem) Buscando todas hospedagem de todos usuarios...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM usuario_has_hospedagem;
        """)

        usu_has_hosps = cursor.fetchall()

        for usu_hosp in usu_has_hosps:
            print(usu_hosp)

        cursor.close()
        conexao.close()

        return usu_has_hosps
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao buscar as hospedagens dos usuarios: {erro}")

def read_all_usuario_has_passagem():
    print(f"(read_all_usuario_has_passagem) Buscando todas passagens de todos usuarios...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM usuario_has_passagem;
        """)
        
        usu_has_pas = cursor.fetchall()

        for usu_pas in usu_has_pas:
            print(usu_pas)

        cursor.close()
        conexao.close()

        return usu_has_pas
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao buscar as passagens dos usuarios: {erro}")

# update

def update_usuario(cpf, nome, email, senha):
    print(f"(update_usuario) Atualizando o usuario {nome}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            UPDATE usuario SET nome = %s, email = %s, senha = %s WHERE cpf = %s)
        """, (nome, email, senha, cpf))

        conexao.commit()

        cursor.close()
        conexao.close()

        print(f'Usuario com cpf {cpf} atualizado com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao atualizar o usuario: {erro}")


def update_estado(idestado, nome_estado):
    print(f"(update_estado) Atualizando o estado {nome_estado}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            UPDATE estado SET nome_estado = %s WHERE idestado = %s);
            """, (nome_estado, idestado))
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print(f"Estado {idestado} atualizado com sucesso!")
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao atualizar o estado: {erro}")

def update_cidade(idcidade, nome_cidade, idestado):
    print(f"(update_cidade) Atualizando a cidade {nome_cidade}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            UPDATE cidade SET nome_cidade = %s, idestado = %s WHERE idcidade = %s);
        """, (nome_cidade, idestado, idcidade))

        conexao.commit()

        cursor.close()
        conexao.close()

        print(f'Cidade {idcidade} atualizada com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao atualizar a cidade: {erro}")

def update_endereco(idendereco, rua, numero, idcidade):
    print(f"(update_endereco) Atualizando o endereço {idendereco}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            UPDATE endereco SET rua = %s, numero = %s, idcidade = %s WHERE idendereco = %s);
            """, (rua, numero, idcidade, idendereco))
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print(f'Endereço {idendereco} atualizado com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao atualizar o endereco: {erro}")

def update_destinos(iddestino, descriçao, fotos, idcidade):
    print(f"(update_destinos) Atualizando o destino {iddestino}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            UPDATE destinos SET descriçao = %s, fotos = %s, idcidade = %s WHERE iddestino = %s);
            """, (descriçao, fotos, idcidade, iddestino))
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print(f'Destino com atualizado com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao atualizar o destino: {erro}")
 
def update_origem(idorigem, idendereco):
    print(f"(update_origem) Atualiando a origem {idorigem}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            UPDATE origem SET idendereco = %s WHERE idorigem = %s);
            """, (idendereco, idorigem))
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print(f'Origem {idorigem} atualizado com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao atualizar a origem: {erro}")
 
def update_classevoo(idclassevoo, nomeclassevoo, preco_classe):
    print(f"(update_classevoo) Atualizando a classe {idclassevoo}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            UPDATE classevoo SET nomeclassevoo = %s, preco_classe = %s WHERE idclassevoo = %s);
            """, (nomeclassevoo, preco_classe, idclassevoo))
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print(f'Classe {idclassevoo} atualizada com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao atualizar a classe do voo: {erro}")

def update_passagem(idpassagem, data_ida, data_volta, idorigem, iddestino, duração, companhia_aerea, qtde_pessoas, idclassevoo):
    print(f"(update_passagem) Atualizando a passagem {idpassagem}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            UPDATE passagem SET data_ida = %s, data_volta = %s, idorigem = %s, iddestino = %s, duração = %s, companhia_aerea = %s, qtde_pessoas = %s, idclassevoo = %s WHERE idpassagem = %s);
            """, (data_ida, data_volta, idorigem, iddestino, duração, companhia_aerea, qtde_pessoas, idclassevoo, idpassagem)) 
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print(f'Passagem {idpassagem} atualizada com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao atualizar a passagem: {erro}")
 
def update_hotel(idhotel, nome_hotel, qtdehospedes, qtdequartos, idendereco):
    print(f"(update_hotel) Atualizando o hotel {idhotel}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            UPDATE hotel SET nome_hotel = %s, qtdehospedes = %s, qtdequartos = %s, idendereco = %s WHERE idhotel = %s);
            """, (nome_hotel, qtdehospedes, qtdequartos, idendereco, idhotel)) 
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print(f'Hotel {idhotel} atualizado com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao atualizar o hotel: {erro}")
 
def update_hospedagem(idhospedagem, idhotel, precos, entrada, saida):
    print(f"(update_hospagem) Atualizando a hospedagem {idhospedagem}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            UPDATE hospedagem SET idhotel = %s, precos = %s, entrada = %s, saida = %s WHERE idhospedagem = %s);
            """, (idhotel, precos, entrada, saida, idhospedagem)) 
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print(f'Hosdagem {idhospedagem} atualizada com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao atualizar a hospedagem: {erro}")
            
def update_usuario_has_hospedagem(cpf, idhospedagem, comentario):
    print(f"(update_usuario_has_hospedagem) Atualizando a hospedagem do usuario {cpf}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            UPDATE usuario_has_hospedagem SET comentario = %s WHERE cpf = %s AND idhospedagem = %s);
            """, (comentario, cpf, idhospedagem)) 
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print(f'Usuario com cpf {cpf}, e id de hospedagem {idhospedagem} atualizado com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao atualizar a hospedagem do usuario: {erro}")

def update_usuario_has_passagem(cpf, idpassagem, comentario):
    print(f"(update_usuario_has_passagem) Atualizando a passagem do usuario {cpf}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            UPDATE usuario_has_hospedagem SET comentario = %s WHERE cpf = %s AND idpassagem = %s);
            """, (comentario, cpf, idpassagem)) 
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print(f'Usuario com cpf {cpf}, e id de passagem {idpassagem} atualizado com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao atualizar a passagem do usuario: {erro}")

# delete

def delete_usuario(cpf):
    print(f"(delette_usuario) Deletando o usuario {cpf}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            DELETE FROM usuario WHERE cpf = %s)
        """, (cpf,))

        conexao.commit()

        cursor.close()
        conexao.close()

        print(f'Usuario com cpf {cpf} deletado com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao deletar o usuario: {erro}")


def delete_estado(idestado):
    print(f"(update_estado) Deletando o estado {idestado}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            DELETE FROM estado WHERE idestado = %s)
        """, (idestado,))
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print(f"Estado {idestado} deletado com sucesso!")
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao deletar o estado: {erro}")

def delete_cidade(idcidade):
    print(f"(delete_cidade) Deletando a cidade {idcidade}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            DELETE FROM cidade WHERE idcidade = %s)
        """, (idcidade,))

        conexao.commit()

        cursor.close()
        conexao.close()

        print(f'Cidade {idcidade} deletada com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao deletar a cidade: {erro}")

def delete_endereco(idendereco):
    print(f"(delete_endereco) Deletando o endereço {idendereco}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            DELETE FROM endereco WHERE idendereco = %s)
        """, (idendereco,))
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print(f'Endereço {idendereco} deletado com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao deletar o endereco: {erro}")

def delete_destinos(iddestino):
    print(f"(delete_destinos) Deletando o destino {iddestino}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            DELETE FROM destinos WHERE iddestino = %s)
        """, (iddestino,))
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print(f'Destino {iddestino} deletado com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao deletar o destino: {erro}")
 
def delete_origem(idorigem):
    print(f"(delete_origem) Deletando a origem {idorigem}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            DELETE FROM origem WHERE idorigem = %s)
        """, (idorigem,))
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print(f'Origem {idorigem} deletada com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao deletar a origem: {erro}")
 
def delete_classevoo(idclassevoo):
    print(f"(delete_classevoo) Deletando a classe {idclassevoo}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            DELETE FROM classevoo WHERE idclassevoo = %s)
        """, (idclassevoo,))
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print(f'Classe {idclassevoo} deletada com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao deletar a classe do voo: {erro}")

def delete_passagem(idpassagem):
    print(f"(delete_passagem) Deletando a passagem {idpassagem}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            DELETE FROM passagem WHERE idpassagem = %s)
        """, (idpassagem,))
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print(f'Passagem {idpassagem} deletada com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao deletar a passagem: {erro}")
 
def delete_hotel(idhotel):
    print(f"(delete_hotel) Deletando o hotel {idhotel}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            DELETE FROM hotel WHERE idhotel = %s)
        """, (idhotel,))
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print(f'Hotel {idhotel} deletado com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao deletar o hotel: {erro}")
 
def delete_hospedagem(idhospedagem):
    print(f"(delete_hospagem) Deletando a hospedagem {idhospedagem}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            DELETE FROM hospedagem WHERE idhospedagem = %s)
        """, (idhospedagem,)) 
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print(f'Hosdagem {idhospedagem} deletada com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao deletar a hospedagem: {erro}")
            
def delete_usuario_has_hospedagem(cpf, idhospedagem):
    print(f"(delete_usuario_has_hospedagem) Deletando a hospedagem do usuario {cpf}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            DELETE FROM usuario_has_hospedagem WHERE cpf = %s AND idhospedagem = %s)
        """, (cpf, idhospedagem,)) 
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print(f'Usuario com cpf {cpf}, e id de hospedagem {idhospedagem} deletado com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao deletar a hospedagem do usuario: {erro}")

def delete_usuario_has_passagem(cpf, idpassagem):
    print(f"(delete_usuario_has_passagem) Deletando a passagem do usuario {cpf}...")
    try:
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        cursor = conexao.cursor()
        cursor.execute("""
            DELETE FROM usuario_has_passagem WHERE cpf = %s AND idpassagem = %s)
        """, (cpf, idpassagem,))
        
        conexao.commit()

        cursor.close()
        conexao.close()

        print(f'Usuario com cpf {cpf}, e id de passagem {idpassagem} deletado com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao deletar a passagem do usuario: {erro}")

def main():
    conexao = get_conexao_postgres()

    criar_tabela_usuario(conexao)
    criar_tabela_estado(conexao)
    criar_tabela_cidade(conexao)
    criar_tabela_endereco(conexao)
    criar_tabela_destinos(conexao)
    criar_tabela_origem(conexao)
    criar_tabela_classevoo(conexao)
    criar_tabela_passagem(conexao)
    criar_tabela_hotel(conexao)
    criar_tabela_hospedagem(conexao)
    criar_tabela_usuario_has_hospedagem(conexao)
    criar_tabela_usuario_has_passagem(conexao)

    conexao.close()

    read_all_usuario()
    print()
    read_all_estado()
    print()
    read_all_cidade()
    print()
    read_all_endereco()
    print()
    read_all_destinos()
    print()
    read_all_origem()
    print()
    read_all_classevoo()
    print()
    read_all_passagem()
    print()
    read_all_hotel()
    print()
    read_all_hospedagem()
    print()
    read_all_usuario_has_hospedagem()
    print()
    read_all_usuario_has_passagem()
    print()

if __name__ == "__main__":
    main