import os
import pyTelegramBotAPI
import requests
from bs4 import BeautifulSoup
import celery

class GameBot:

    def __init__(self):
        self.bot = pyTelegramBotAPI.Bot(os.getenv("BOT_TOKEN"))
        self.group_id = os.getenv("GROUP_ID")

    def get_free_games(self):
        free_games = []
        for platform in ["steam", "epicgames", "gog", "primegaming"]:
            response = requests.get(f"https://www.isthereanydeal.com/specials/{platform}")
            soup = BeautifulSoup(response.content, "html.parser")
            for game in soup.find_all("a", class_="game-link"):
                free_games.append(game["href"])
        return free_games

    def get_best_deals(self):
        best_deals = []
        response = requests.get("https://www.isthereanydeal.com/")
        soup = BeautifulSoup(response.content, "html.parser")
        for deal in soup.find_all("div", class_="deal-item"):
            best_deals.append({
                "title": deal["data-title"],
                "url": deal["data-url"],
                "price": deal["data-price"],
                "old_price": deal["data-old_price"],
            })
        return best_deals

    @celery.task()
    def send_notifications(self):
        free_games = self.get_free_games()
        best_deals = self.get_best_deals()
        self.bot.send_message(self.group_id, "Jogos gratuitos da semana:")
        for game in free_games:
            self.bot.send_message(self.group_id, f"* {game}")
        self.bot.send_message(self.group_id, "Melhores promoções da semana:")
        for deal in best_deals:
            self.bot.send_message(self.group_id, f"* {deal['title']}: {deal['price']} ({deal['old_price']} antes)")


if __name__ == "__main__":
    bot = GameBot()
    # Definimos a expressão cron para executar a cada 2 dias às 8 horas da manhã
    schedule = celery.schedules.crontab(hour=8, day_of_week='*', interval=2)
    # Agendamos a tarefa `send_notifications()` para ser executada de acordo com a expressão cron
    celery.task.schedule(schedule, bot.send_notifications)

    # Ligamos o manipulador de mensagens do Telegram
    bot.bot.on_message(bot.on_message)

    # Iniciamos o Celery
    celery.worker.start()
