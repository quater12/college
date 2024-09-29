token='8032025145:AAEMQpXsUgmPmEeTwcs5nIA7pCxRein4T9o'
import telebot

bot=telebot.TeleBot(token=token)


@bot.message_handler(content_types=['text'])
def message_received(message):
    if message.text == "exit":
        exit(0)
    print(message)
    bot.send_message(chat_id=message.from_user.id, text=message.text)

bot.polling(True)

