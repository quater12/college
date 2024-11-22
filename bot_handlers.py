import logging
import telebot
from telebot import types
from utils import TOKEN
logging.basicConfig(level=logging.INFO)


def log_message(func):
    def wrapper(message, *args, **kwargs):
        logging.info(f"Отримано повідомлення від {message.chat.id}: {message.text}")
        return func(message, *args, **kwargs)

    return wrapper


bot = telebot.TeleBot(TOKEN)

selected_seedling = None

logging.basicConfig(level=logging.INFO)


@bot.message_handler(commands=['start'])
@log_message
def send_welcome(message):
    bot.reply_to(message,
                 'Привіт! Я бот, який продає саженці дерев. Використайте команду /catalog, щоб переглянути наш каталог.')


@bot.message_handler(commands=['catalog'])
@log_message
def send_catalog(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    apple_button = types.KeyboardButton("Яблуня")
    pear_button = types.KeyboardButton("Груша")
    grape_button = types.KeyboardButton("Виноград")
    plum_button = types.KeyboardButton("Слива")

    markup.add(apple_button, pear_button, grape_button, plum_button)
    bot.send_message(message.chat.id, "Оберіть тип саженця:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in ["Яблуня", "Груша", "Виноград", "Слива"])
@log_message
def send_seedling_varieties(message):
    global selected_seedling
    selected_seedling = message.text

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    varieties = get_varieties(selected_seedling)

    for variety, link in varieties:
        markup.add(types.KeyboardButton(variety))

    bot.send_message(message.chat.id, f"Оберіть сорт {selected_seedling.lower()}:", reply_markup=markup)


def get_varieties(seedling_type):
    if seedling_type == "Яблуня":
        return [
            ("Сорт Яблуні 1", "https://example.com/apple1"),
            ("Сорт Яблуні 2", "https://example.com/apple2"),
            ("Сорт Яблуні 3", "https://example.com/apple3")
        ]
    elif seedling_type == "Груша":
        return [
            ("Сорт Груші 1", "https://example.com/pear1"),
            ("Сорт Груші 2", "https://example.com/pear2"),
            ("Сорт Груші 3", "https://example.com/pear3")
        ]
    elif seedling_type == "Виноград":
        return [
            ("Сорт Винограду 1", "https://example.com/grape1"),
            ("Сорт Винограду 2", "https://example.com/grape2"),
            ("Сорт Винограду 3", "https://example.com/grape3")
        ]
    elif seedling_type == "Слива":
        return [
            ("Сорт Сливи 1", "https://example.com/plum1"),
            ("Сорт Сливи 2", "https://example.com/plum2"),
            ("Сорт Сливи 3", "https://example.com/plum3")
        ]


@bot.message_handler(func=lambda message: message.text.startswith("Сорт"))
@log_message
def send_variety_info(message):
    variety = message.text
    link = get_link_for_variety(variety)

    bot.send_message(
        message.chat.id,
        f"Ви обрали {selected_seedling} ({variety}) - [Посилання на сайт]({link})",
        parse_mode='Markdown'
    )

    ask_more(message.chat.id)


def get_link_for_variety(variety):
    links = {
        "Сорт Яблуні 1": "https://example.com/apple1",
        "Сорт Яблуні 2": "https://example.com/apple2",
        "Сорт Яблуні 3": "https://example.com/apple3",
        "Сорт Груші 1": "https://example.com/pear1",
        "Сорт Груші 2": "https://example.com/pear2",
        "Сорт Груші 3": "https://example.com/pear3",
        "Сорт Винограду 1": "https://example.com/grape1",
        "Сорт Винограду 2": "https://example.com/grape2",
        "Сорт Винограду 3": "https://example.com/grape3",
        "Сорт Сливи 1": "https://example.com/plum1",
        "Сорт Сливи 2": "https://example.com/plum2",
        "Сорт Сливи 3": "https://example.com/plum3"
    }
    return links.get(variety, "")


def ask_more(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    yes_button = types.KeyboardButton("Так")
    no_button = types.KeyboardButton("Ні")

    markup.add(yes_button, no_button)
    bot.send_message(chat_id, "Чи бажаєте придбати щось крім цього?", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Так")
@log_message
def handle_more_purchase(message):
    send_catalog(message)


@bot.message_handler(func=lambda message: message.text == "Ні")
@log_message
def handle_no_more_purchase(message):
    bot.reply_to(message, "Дякую за використання бота! Повертаю вас на головний екран.")


@bot.message_handler(commands=['help'])
@log_message
def send_help(message):
    help_message = (
        "Доступні команди:\n"
        "/start - Почати спілкування з ботом\n"
        "/catalog - Переглянути каталог саженців\n"
        "/help - Отримати допомогу\n"
        "Надішліть 'exit', щоб завершити роботу бота."
    )
    bot.reply_to(message, help_message)


@bot.message_handler(func=lambda message: message.text.lower() == 'exit')
@log_message
def exit_bot(message):
    bot.reply_to(message, "Дякую за використання бота! До побачення!")
    bot.stop_polling()


if __name__ == '__main__':
    bot.polling(none_stop=True)