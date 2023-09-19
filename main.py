import os

from telegram.ext import Updater, CommandHandler


def start(update, context):
    # Envia uma mensagem de boas-vindas ao grupo
    context.bot.send_message(chat_id=context.channel_id, text="Olá, pessoal!")


def main():
    # Obtém o token do bot e o ID do grupo do ambiente
    BOT_TOKEN = os.environ['BOT_TOKEN']
    GROUP_ID = os.environ['GROUP_ID']

    # Cria um atualizador do bot
    updater = Updater(token=BOT_TOKEN)

    # Registra o manipulador de comandos
    updater.dispatcher.add_handler(CommandHandler('start', start))

    # Inicia o bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
