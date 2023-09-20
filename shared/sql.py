def sql_consulta_de_jogos():
    return f"""SELECT CONCAT(plataforma, ': ', descricao) AS plataforma_descricao FROM lista_de_jogos ORDER BY plataforma"""

