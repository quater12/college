import telebot
from telebot import types

TOKEN = '7977873751:AAGBR99xltXhtU6haSd3j9LZC3BzIWzJWjc'
bot = telebot.TeleBot(TOKEN)

selected_seedling = None

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привіт! Я бот, який продає саженці дерев. Використайте команду /catalog, щоб переглянути наш каталог.')

@bot.message_handler(commands=['catalog'])
def send_catalog(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    apple_button = types.KeyboardButton("Яблуня")
    pear_button = types.KeyboardButton("Груша")
    grape_button = types.KeyboardButton("Виноград")
    plum_button = types.KeyboardButton("Слива")

    markup.add(apple_button, pear_button, grape_button, plum_button)
    bot.send_message(message.chat.id, "Оберіть тип саженця:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["Яблуня", "Груша", "Виноград", "Слива"])
def send_seedling_varieties(message):
    global selected_seedling
    selected_seedling = message.text

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    if selected_seedling == "Яблуня":
        varieties = [
            ("Сорт Яблуні 1", "https://example.com/apple1"),
            ("Сорт Яблуні 2", "https://example.com/apple2"),
            ("Сорт Яблуні 3", "https://example.com/apple3")
        ]
    elif selected_seedling == "Груша":
        varieties = [
            ("Сорт Груші 1", "https://example.com/pear1"),
            ("Сорт Груші 2", "https://example.com/pear2"),
            ("Сорт Груші 3", "https://example.com/pear3")
        ]
    elif selected_seedling == "Виноград":
        varieties = [
            ("Сорт Винограду 1", "https://example.com/grape1"),
            ("Сорт Винограду 2", "https://example.com/grape2"),
            ("Сорт Винограду 3", "https://example.com/grape3")
        ]
    elif selected_seedling == "Слива":
        varieties = [
            ("Сорт Сливи 1", "https://example.com/plum1"),
            ("Сорт Сливи 2", "https://example.com/plum2"),
            ("Сорт Сливи 3", "https://example.com/plum3")
        ]

    for variety, link in varieties:
        markup.add(types.KeyboardButton(variety))

    bot.send_message(message.chat.id, f"Оберіть сорт {selected_seedling.lower()}:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text.startswith("Сорт"))
def send_variety_info(message):
    variety = message.text
    link = ""

    if selected_seedling == "Яблуня":
        if variety == "Сорт Яблуні 1":
            link = "https://example.com/apple1"
        elif variety == "Сорт Яблуні 2":
            link = "https://example.com/apple2"
        elif variety == "Сорт Яблуні 3":
            link = "https://example.com/apple3"
    elif selected_seedling == "Груша":
        if variety == "Сорт Груші 1":
            link = "https://example.com/pear1"
        elif variety == "Сорт Груші 2":
            link = "https://example.com/pear2"
        elif variety == "Сорт Груші 3":
            link = "https://example.com/pear3"
    elif selected_seedling == "Виноград":
        if variety == "Сорт Винограду 1":
            link = "https://example.com/grape1"
        elif variety == "Сорт Винограду 2":
            link = "https://example.com/grape2"
        elif variety == "Сорт Винограду 3":
            link = "https://example.com/grape3"
    elif selected_seedling == "Слива":
        if variety == "Сорт Сливи 1":
            link = "https://example.com/plum1"
        elif variety == "Сорт Сливи 2":
            link = "https://example.com/plum2"
        elif variety == "Сорт Сливи 3":
            link = "https://example.com/plum3"

    bot.send_message(
        message.chat.id,
        f"Ви обрали {selected_seedling} ({variety}) - [Посилання на сайт]({link})",
        parse_mode='Markdown'
    )

    ask_more(message.chat.id)

def ask_more(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    yes_button = types.KeyboardButton("Так")
    no_button = types.KeyboardButton("Ні")

    markup.add(yes_button, no_button)
    bot.send_message(chat_id, "Чи бажаєте придбати щось крім цього?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Так")
def handle_more_purchase(message):
    send_catalog(message)

@bot.message_handler(func=lambda message: message.text == "Ні")
def handle_no_more_purchase(message):
    bot.reply_to(message, "Дякую за використання бота! Повертаю вас на головний екран.")

@bot.message_handler(commands=['help'])
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
def exit_bot(message):
    bot.reply_to(message, "Дякую за використання бота! До побачення!")
    bot.stop_polling()

if __name__ == '__main__':
    bot.polling()
