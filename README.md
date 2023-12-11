# Trab_BD
Trabalho de banco de dados 4°bimestre

Orientações para o funcionamento do codigo

1° Visual studio code
A primeira coisa a se fazer é abrir o codigo em alguma plataforma que rode python, recomendamos o Studio Visual Code

2° Extensões
É necessário que você baixe a extensão de python, que você tambem precisará baixar python na sua máquina

3° Terminal
Abra o terminal ou o Prompt de comando, que aparecem assim que você os pesquisa nos aplicativos, e digite
"pip install sql alchemy" 
"pip install flask" 
“pip install psycopg2”
“pip install flask_sqlalchemy”

4° Engine
Você precisará criar um servidor no PgAdmin, assim que criado substitua 

engine =  create_engine('postgresql://postgres:postgres@localhost:5432/X')

No segundo postgres coloque seu nome de usuário, no terceiro sua senha, no localhost seu endereço, 5432 pela sua senha, e X pelo nome do seu banco de dados.



