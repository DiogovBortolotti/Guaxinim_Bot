import telebot
import os

from fun.confere_jogos import confere_gog, confere_epic


bot = telebot.TeleBot(os.environ['TOKEN_TELEGRAM'])

@bot.message_handler(commands= 'Jogos')
def conferir_jogos_gratis_semana(message):
    gog = confere_gog()
    epic = confere_epic()
    bot.send_message(message.chat.id, f"""ㅤㅤㅤㅤㅤ!JOGOS DA SEMANA!\n\n\nGOG:\n{gog}\n\nEPIC:\n{epic}""")


#func=lambda message: True sempre automatico
@bot.message_handler(commands=['Ajuda', 'Comandos', 'Help', 'Start'])
def mensagem_inicial(message):
    bot.send_message(message.chat.id, f""" Ola! segue os meus comandos: \n/Jogos  - Para saber a rotação da semana """)
    #bot.reply_to(message.chat.id, f""" As Opções  """)

# Inicie o bot
bot.polling()
