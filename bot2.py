import telebot
from telebot import types

TOKEN = '7977873751:AAGBR99xltXhtU6haSd3j9LZC3BzIWzJWjc'
bot = telebot.TeleBot(TOKEN)

selected_seedling = None


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,
                 'Привіт! Я бот, який продає саженці дерев. Використайте команду /catalog, щоб переглянути наш каталог.')


@bot.message_handler(commands=['catalog'])
def send_catalog(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    apple_button = types.KeyboardButton("Яблуня")
    pear_button = types.KeyboardButton("Груша")
    cherry_button = types.KeyboardButton("Виноград")
    plum_button = types.KeyboardButton("Слива")

    markup.add(apple_button, pear_button, cherry_button, plum_button)
    bot.send_message(message.chat.id, "Оберіть тип саженця:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in ["Яблуня", "Груша", "Вишня", "Слива"])
def send_seedling_varieties(message):
    global selected_seedling
    selected_seedling = message.text  # Зберігаємо вибраний тип саженця

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    if selected_seedling == "Яблуня":
        varieties = [
            ("Ред Мун", "https://agro-market.net/ua/catalog/item/yablonya_krasnomyasaya_red_mun_red_moon_letniy_sort_sredniy_srok_sozrevaniya/"),
            ("Фуджі", "https://agro-market.net/ua/catalog/item/7569/"),
            ("Голден Делішес", "https://agro-market.net/ua/catalog/item/yablonya_golden_delishes_1/")
        ]
    elif selected_seedling == "Груша":
        varieties = [
            ("Киргиська", "https://agro-market.net/ua/catalog/item/grusha_kirgizskaya_zimnyaya/"),
            ("Медова", "https://agro-market.net/ua/catalog/item/grusha_kolonovidnaya_medovaya_new/"),
            ("Дюшес", "https://agro-market.net/ua/catalog/item/5811/")
        ]
    elif selected_seedling == "Виноград":
        varieties = [
            ("Йоханітер",
             "https://agro-market.net/ua/catalog/item/vinograd_vegetiruyushchiy_vinnyy_yokhaniter_/"),
            ("Аркадія", "https://agro-market.net/ua/catalog/item/7684/"),
            ("Водограй", "https://agro-market.net/ua/catalog/item/10079/")
        ]
    elif selected_seedling == "Слива":
        varieties = [
            ("Рубі Кранч", "https://agro-market.net/ua/catalog/item/sliva_krasnomyasaya_rubi_kranch_osenniy_sort_pozdniy_srok_sozrevaniya/"),
            ("Пінк Сатурн", "https://agro-market.net/ua/catalog/item/sliva_diploidnaya_pink_saturn_krupnoplodnyy_sort_sredniy_srok_sozrevaniya/"),
            ("Біла медова", "https://agro-market.net/ua/catalog/item/7580/")
        ]

    for variety, link in varieties:
        markup.add(types.KeyboardButton(variety))

    bot.send_message(message.chat.id, f"Оберіть сорт {selected_seedling}:", reply_markup=markup)


@bot.message_handler(
    func=lambda message: message.text in ["Ред Мун", "Фуджі", "Голден Делішес", "Киргиська", "Медова",
                                          "Дюшес", "Йоханітер", "Аркадія", "Водограй", "Рубі Кранч",
                                          "Пінк Сатурн", "Біла медова"])
def send_variety_info(message):
    variety = message.text
    link = ""

    if selected_seedling == "Яблуня":
        if variety == "Ред Мун":
            link = "https://agro-market.net/ua/catalog/item/yablonya_krasnomyasaya_red_mun_red_moon_letniy_sort_sredniy_srok_sozrevaniya/"
        elif variety == "Фуджі":
            link = "https://agro-market.net/ua/catalog/item/7569/"
        elif variety == "Голден Делішес":
            link = "https://agro-market.net/ua/catalog/item/yablonya_golden_delishes_1/"
    elif selected_seedling == "Груша":
        if variety == "Киргиська":
            link = "https://agro-market.net/ua/catalog/item/grusha_kirgizskaya_zimnyaya/"
        elif variety == "Медова":
            link = "https://agro-market.net/ua/catalog/item/grusha_kolonovidnaya_medovaya_new/"
        elif variety == "Дюшес":
            link = "https://agro-market.net/ua/catalog/item/5811/"
    elif selected_seedling == "Виноград":
        if variety == "Йоханітер":
            link = "https://agro-market.net/ua/catalog/item/vinograd_vegetiruyushchiy_vinnyy_yokhaniter_/"
        elif variety == "Аркадія":
            link = "https://agro-market.net/ua/catalog/item/7684/"
        elif variety == "Водограй":
            link = "https://agro-market.net/ua/catalog/item/10079/"
    elif selected_seedling == "Слива":
        if variety == "Рубі Кранч":
            link = "https://agro-market.net/ua/catalog/item/sliva_krasnomyasaya_rubi_kranch_osenniy_sort_pozdniy_srok_sozrevaniya/"
        elif variety == "Пінк Сатурн":
            link = "https://agro-market.net/ua/catalog/item/sliva_diploidnaya_pink_saturn_krupnoplodnyy_sort_sredniy_srok_sozrevaniya/"
        elif variety == "Біла Медова":
            link = "https://agro-market.net/ua/catalog/item/7580/"

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
    send_welcome(message)


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
