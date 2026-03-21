import pymysql 
import pymysql.cursors 

# Arquivo para trabalhar com banco de daddos  e fazer as operaçoes 

conexao = pymysql.connect (
    host = "localhost",          # endereço do servidor (local = "localhost")
    user = "root",        # usuario do mySQL
    passwd = "",        # banco que voce ja criou 
    database = "bd_livrariaonline",  # porta padrão do MySQL (opcional)
    port = 3306
)

cursor = conexao.cursor(pymysql.cursors.DictCursor) 


try:
#     # --- INsert: adicionar um novo registro ---
#     sql_insert ="INSERT INTO clientes (nome, email ) VALUES (%s, %s)"
#     cursor.execute(sql_insert, ("Ana Lima ","ana@email.com"))
#     conexao.commit() # <- confimar o INSERT
#     print("Inserindo com sucesso! ID:", cursor.lastrowid)

#     # --- UPDATE: atualizar um registro existente ---
#     sql_update = "UPDATE clientes SET email = %s WHARE id_cliente = %s"
#     cursor.execute(sql_update, ("novo@email.com", 1))
#     conexao.commit() # <- confirma o UPDATE 
#     print("Linhas afestadas:", cursor.rowcount)

# --- DELETE: remover um registro ---
    cursor.execute("DELETE FROM clientes WHERE id_cliente = %s", (6))
    conexao.commit()

except Exception as erro:
    conexao.rollback() # <- desfazer tudo se algo deu errado
    print("Erro! Operação revertida:", erro)

finally:
    cursor.close()
    conexao.close() # -> fechar a conexao com o banco de dados 

