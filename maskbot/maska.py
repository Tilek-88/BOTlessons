import telebot
import config

from telebot import types
 
bot = telebot.TeleBot(config.TOKEN)
 
@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(":woman:🏻⚕ Продавец-фармацевт")
    item2 = types.KeyboardButton("🧴 Покупатель")
 
    markup.add(item1, item2)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы помочь, Вам!".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
# RUN
bot.polling(none_stop=True)