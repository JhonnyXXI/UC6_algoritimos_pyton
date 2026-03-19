import pymysql
import pymysql.cursors

conexao = pymysql.connect (
    host = "localhost",          # endereço do servidor (local = "localhost")
    user = "root",        # usuario do mySQL
    passwd = "",        # banco que voce ja criou 
    database = "bd_livrariaonline",  # porta padrão do MySQL (opcional)
    port = 3306
)

cursor = conexao.cursor(pymysql.cursors.DictCursor)

cursor.execute("SELECT * FROM clientes")
todos = cursor.fetchall()

for cliente in todos:
    print(cliente["nome"], cliente["email"])

    print(todos)