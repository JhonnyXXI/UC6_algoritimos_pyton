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

# for cliente in todos:
#     print(cliente["nome"],",", cliente["email"],",",cliente["telefone"])

# --- Buscar um unico registro por ID ---

cursor.execute("SELECT * FROM clientes WHERE id_cliente = 1")

cliente = cursor.fetchone()
print(cliente) # {'id':1. 'nome': "Maria', 'email': '...'}

# --- Buscar com filtro dinâmico ---

nome_busca = "Ursula%"
cursor.execute("SELECT * FROM clientes WHERE nome  LIKE%s",(nome_busca),)

resultado = cursor.fetchall()

print(resultado)