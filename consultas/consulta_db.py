
import mysql.connector

from shared.settings import DATABASE,HOST,SENHA,USUARIO

class ConexaoMysql:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host=HOST,
            user=USUARIO,
            password=SENHA,
            database=DATABASE
        )
    
    def fechar_conexao(self):
        self.conn.close()

    def consultar_dados(self, consulta):
        cursor = self.conn.cursor()
        cursor.execute(consulta)
        resultados = cursor.fetchall()
        cursor.close()
        return resultados
    
    def inserir_dados(self, insert):
        cursor = self.conn.cursor()
        cursor.execute(insert)
        self.conn.commit()
        cursor.close()