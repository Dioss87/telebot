import telebot
import requests

# подключаем токен; получаем его на @fatherbot)
bot = telebot.TeleBot("7679283944:AAH7kCXfNvemAvG0ugqzHzb04LF_TyBkTgg")


# Обработка команд: /start, /help, etc (параметр указываем без слэша)
# commands для команд; content_types для конкр. типа: текст, фото, видео, док-ты, контакты, анимация и пр.
@bot.message_handler(commands=["start"])
def send_welcome_msg(message):
    bot.send_message(message.chat.id, "Привет, напиши 'курсы', чтобы узнать текущий курс доллара и евро.")


# фун-я для получения курсов валют
def get_exchange_rate():
    url = "https://www.cbr-xml-daily.ru/daily_json.js"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        rub_to_eur = data["Valute"]["EUR"]["Value"]
        rub_to_usd = data["Valute"]["USD"]["Value"]
        return f"1 USD = {rub_to_usd} RUB\n1 EUR = {rub_to_eur} RUB"
    except requests.exceptions.RequestException as e:
        return f"Ошибка при запросе данных: {e}"
    except KeyError:
        return "Ошибка: Неверный формат от сервера."


# обработка сообщений от пользователя, реагируем на слово -курсы
@bot.message_handler(func=lambda message: message.text.strip().lower() == "курсы")
def send_exchange_rates(message):
    rates = get_exchange_rate()
    bot.send_message(message.chat.id, rates)


# делаем проверку, что код запускается из основого файла, а не как импорт-й модуль в другом скрипте;
# по сути точка входа! важный пункт!
if __name__ == "__main__":
    print("Bot running...")
    bot.polling(non_stop=True, timeout=10)

