import mysql.connector

# Classe de conexao com o banco de dados
class Conexao:
        def __init__(self):
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='mysql#123',
                database='ocorrenciasql'
            )
            self.cursor = self.connection.cursor()

        def get_ocorrencia(self, tipo_lista):
            sql=''
            if tipo_lista=="4":
                sql = 'SELECT * FROM ocorrenciasql'
                self.cursor.execute(sql)
            else:
                sql = 'SELECT * FROM ocorrenciasql where tipo=%s'
                data = (tipo_lista, )
                self.cursor.execute(sql, data)
            lista_ocorrencias = self.cursor.fetchall()

            return lista_ocorrencias

        def post_ocorrencia(self, titulo, tipo, descricao):
            sql='INSERT INTO ocorrenciasql(titulo, tipo, descricao) VALUES (%s,%s,%s)'
            data=(titulo, tipo, descricao)

            self.cursor.execute(sql, data)
            self.connection.commit()

            userId = self.cursor.lastrowid
            return userId
        
        def search_ocorrencia(self, id):
             sql = 'select * from ocorrenciasql where id=%s'
             data = (id, )

             self.cursor.execute(sql, data)
             lista_ocorrencia = self.cursor.fetchall()

             return lista_ocorrencia

        def delete_ocorrencia(self, id):
            sql='DELETE from ocorrenciasql where id=%s'
            data=(id,)

            self.cursor.execute(sql, data)
            self.connection.commit()

            recordAffect = self.cursor.rowcount

            return recordAffect

        def close_conexao(self):
            self.cursor.close()
            self.connection.close()
