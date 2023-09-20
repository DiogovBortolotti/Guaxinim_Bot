import requests
from bs4 import BeautifulSoup

def confere_epic():
    response = requests.get("https://www.epicgames.com/store/pt-BR/free-games")
    data = response.content.decode("utf-8")
    gog_jogos = []
    for jogo in BeautifulSoup(data, features="html.parser").find_all("div", class_="GameCard__TitleWrapper"):
        gog_jogos.append(jogo.text)
    if gog_jogos:
        jogo = gog_jogos[0]
        return "\n".join([j['nome'] for j in jogo])
    else:
        return "Não há jogos gratuitos disponíveis nesta semana."


def confere_gog():
    response = requests.get("https://www.gog.com/en/games?priceRange=0,0&order=desc:bestselling")
    data = response.content.decode("utf-8")
    gog_jogos = []
    for jogo in BeautifulSoup(data, features="html.parser").find_all("div", class_="paginated-products-grid grid"):
        gog_jogos.append(jogo.text)
    lista_dos_jogos_gratis_gog = []
    for nome_jogo in gog_jogos:
        for jogos in nome_jogo.split("\n"):
            jogos = jogos.replace("FREEDLC", "").replace("FREE", "") 
            if jogos:
                lista_dos_jogos_gratis_gog.append({"nome": jogos})
                if len(lista_dos_jogos_gratis_gog) == 5:
                    break
    if lista_dos_jogos_gratis_gog:
        return  "\n".join([j['nome'] for j in lista_dos_jogos_gratis_gog])
    else: 
        "Não há jogos gratuitos disponíveis nesta semana."



