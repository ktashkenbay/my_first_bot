
import config
import telebot, requests
from telebot import types
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db



cred = credentials.Certificate("kasym.json")
default_app = firebase_admin.initialize_app(cred, {'databaseURL': 'https://grgrgrw-3bc83.firebaseio.com/'})


bot = telebot.TeleBot(config.token)
# Neoбычный режим
@bot.message_handler(commands = ['start'])

def start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Тарих', 'Физика', 'Биология','География']])
    msg = bot.send_message(message.chat.id, "Салеметсизбе. Категория танданыз", reply_markup = keyboard)
    bot.register_next_step_handler(msg, answer)

@bot.message_handler(content_types = ['text'])
def answer(message):
    if message.text == "Тарих":
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(question) for question in ['dada', 'baba', 'haha', 'gaga', 'fafa']])
        msg = bot.send_message(message.chat.id, "Кандай суракты тандайсыз?", reply_markup = keyboard)
        bot.register_next_step_handler(msg, answer_subject)
    if message.text == "Физика":
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(question) for question in ['do', 'we', 'ba', 'ha', 'by']])
        msg = bot.send_message(message.chat.id, "Кандай суракты тандайсыз?", reply_markup = keyboard)
        bot.register_next_step_handler(msg, answer_subject)
    if message.text == "Биология":
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(question) for question in ['dos', 'wes', 'bas', 'has', 'bys']])
        msg = bot.send_message(message.chat.id, "Кандай суракты тандайсыз?", reply_markup = keyboard)
        bot.register_next_step_handler(msg, answer_subject)
    if message.text == "География":
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(question) for question in ['dosh', 'wesh', 'bash', 'hash', 'bysh']])
        msg = bot.send_message(message.chat.id, "Кандай суракты тандайсыз?", reply_markup = keyboard)
        bot.register_next_step_handler(msg, answer_subject)


        
@bot.message_handler(content_types = ['text'])
def answer_subject(message):
    if message.text == 'dada':
        subject = db.reference('/Тарих/a/dada').get()
        bot.send_message(message.chat.id, subject)
    if message.text == 'baba':
        subject = db.reference('/Тарих/b/baba').get()
        bot.send_message(message.chat.id, subject)
    if message.text == 'haha':
        subject = db.reference('/Тарих/c/haha').get()
        bot.send_message(message.chat.id, subject)
    if message.text == 'gaga':
       subject = db.reference('/Тарих/d/gaga').get()
       bot.send_message(message.chat.id, subject)
    if message.text == 'fafa':
        subject = db.reference('/Тарих/e/dada').get()
        bot.send_message(message.chat.id, subject)
    

    
    
        

'''
@bot.message_handler(content_types=["text"])
def any_msg(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Канал в YouTube",url='https://www.youtube.com/channel/UC_cBsck6NyqzSDaNEfOJ5HQ' )
    url_button2 = types.InlineKeyboardButton(text="YouTube",url='https://www.youtube.com')
    url_button3 = types.InlineKeyboardButton(text="Мой VK",url='https://vk.com/id289417861')
    url_button4 = types.InlineKeyboardButton(text="Мой classroom",url='https://classroom.google.com')
    keyboard.add(url_button, url_button2,url_button3, url_button4)
    bot.send_message(message.chat.id, "Привет, подписывайся на меня в социальных сетях", reply_markup=keyboard)

@bot.message_handler(content_types=["text"])
def geophone(message):
    bot.send_message(message.chat.id, "Хочешь отправить мне свой телефон или местоположение? Отправь да или нет? ", reply_markup=keyboard)
    if message.text == "да":
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
        button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
        keyboard.add(button_phone, button_geo)
        bot.send_message(message.chat.id, "Отправь мне свой номер телефона или поделись местоположением, жалкий человечишка!", reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, "OK", reply_markup=keyboard)


    







    

    keyboard = types.InlineKeyboardMarkup()
    if message.text=='привет':
        bot.send_message(message.chat.id, 'привет,как ваши дела?')
    if message.text == "хорошо":
        bot.send_message(message.chat.id, "Quanyshtymyn!!")
        bot.send_message(message.chat.id, 'Может вам понадобиться наши инлайн кнопки')
    if message.text == "пока нет":
            bot.send_message(message.chat.id, 'OK!!')
    elif message.text == 'давайте':
            keybord = telebot.types.InlineKeyboardMarkup()
       # bot.send_message(message.chat.id, 'Открываю https://classroom.google.com нажмите на ссылку')
            url_button = types.InlineKeyboardButton(text=" k kaba kz",url='https://www.youtube.com/channel/UC_cBsck6NyqzSDaNEfOJ5HQ'.format(message.text))
            url_button2 = types.InlineKeyboardButton(text="ютуб",url='https://www.youtube.com'.format(message.text))
            url_button3 = types.InlineKeyboardButton(text="меня создал",url='https://vk.com/id289417861'.format(message.text))
            url_button4 = types.InlineKeyboardButton(text='classroom',url='https://classroom.google.com'.format(message.text))
            keyboard.add(url_button,url_button2,url_button3,url_button4)
            
    elif message.text == 'открой мне ютуб':
        bot.send_message(message.chat.id, 'Открываю https://www.youtube.com нажмите на ссылку')
        '''





if __name__ == '__main__':
    bot.polling(none_stop=True)
