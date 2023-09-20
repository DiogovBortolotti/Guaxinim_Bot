import telebot

from shared.settings import TOKEN_TELEGRAM
from consultas.consulta_jogos import retona_rotacao_jogos



bot = telebot.TeleBot(TOKEN_TELEGRAM)

@bot.message_handler(commands=['jogos'])
def conferir_jogos_gratis_semana(message):
    mensagem = "ㅤㅤㅤㅤㅤ!JOGOS DA SEMANA!\n\n\n"
    for jogo in retona_rotacao_jogos():
        mensagem += f"{jogo[0]}\n"
    bot.send_message(message.chat.id, mensagem)

#func=lambda message: True sempre automatico
@bot.message_handler(commands=['ajuda', 'comandos', 'help', 'start'])
def mensagem_inicial(message):
    bot.send_message(message.chat.id, f""" Ola! segue os meus comandos: \n/Jogos  - Para saber a rotação da semana """)
    #bot.reply_to(message.chat.id, f""" As Opções  """)

# Inicie o bot
bot.polling()
