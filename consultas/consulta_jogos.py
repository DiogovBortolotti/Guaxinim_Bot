from consultas.consulta_db import ConexaoMysql
from shared.sql import sql_consulta_de_jogos

def retona_rotacao_jogos():
    conexao = ConexaoMysql()
    resultado = conexao.consultar_dados(sql_consulta_de_jogos())
    conexao.fechar_conexao()
    return resultado