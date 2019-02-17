
import config
import telebot, requests
from telebot import types
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db



cred = credentials.Certificate("kasym.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://grgrgrw-3bc83.firebaseio.com/'})


bot = telebot.TeleBot(config.token)
# Neoбычный режим
<<<<<<< HEAD
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
        keyboard.add(*[types.KeyboardButton(question) for question in ['dodo', 'wewe', 'baba', 'haha', 'byby']])
        msg = bot.send_message(message.chat.id, "Кандай суракты тандайсыз?", reply_markup = keyboard)
        bot.register_next_step_handler(msg, answer_subject)
    elif message.text == "Физика":
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(question) for question in ['dodo', 'wewe', 'baba', 'haha', 'byby']])
        msg = bot.send_message(message.chat.id, "Кандай суракты тандайсыз?", reply_markup = keyboard)
        bot.register_next_step_handler(msg, answer_subject)
    elif message.text == "Биология":
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(question) for question in ['dodo', 'wewe', 'baba', 'haha', 'byby']])
        msg = bot.send_message(message.chat.id, "Кандай суракты тандайсыз?", reply_markup = keyboard)
        bot.register_next_step_handler(msg, answer_subject)
    elif message.text == "География":
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(question) for question in ['dodo', 'wewe', 'baba', 'haha', 'byby']])
        msg = bot.send_message(message.chat.id, "Кандай суракты тандайсыз?", reply_markup = keyboard)
        bot.register_next_step_handler(msg, answer_subject)
        
@bot.message_handler(content_types = ['text'])
def answer_subject(message):
    if message.text == 'dodo':
        bot.send_message(message.chat.id, "Басталды 1914 жылы")
    elif message.text == 'wewe':
        bot.send_message(message.chat.id, "Басталды 1770 жылы")
    elif message.text == 'baba':
        bot.send_message(message.chat.id, "Басталды 1980 жылы")
    elif message.text == 'haha':
        bot.send_message(message.chat.id, "Басталды 1875 жылы")
    elif message.text == 'byby':
        bot.send_message(message.chat.id, "Басталды 1941 жылы")


@bot.message_handler(content_types = ['text'])
def answer_subject(message):
    if message.text == 'do':
        bot.send_message(message.chat.id, "Басталды 5418 жылы")
    elif message.text == 'we':
        bot.send_message(message.chat.id, "Басталды 8745 жылы")
    elif message.text == 'ba':
        bot.send_message(message.chat.id, "Басталды 7278 жылы")
    elif message.text == 'ha':
        bot.send_message(message.chat.id, "Басталды 1742 жылы")
    elif message.text == 'by':
        bot.send_message(message.chat.id, "Басталды 7255 жылы")



@bot.message_handler(content_types = ['text'])
def answer_subject(message):
    if message.text == 'dos':
        bot.send_message(message.chat.id, "Басталды 5386 жылы")
    elif message.text == 'wes':
        bot.send_message(message.chat.id, "Басталды 4580 жылы")
    elif message.text == 'bas':
        bot.send_message(message.chat.id, "Басталды 5684 жылы")
    elif message.text == 'has':
        bot.send_message(message.chat.id, "Басталды 5784 жылы")
    elif message.text == 'bys':
        bot.send_message(message.chat.id, "Басталды 6544 жылы")



@bot.message_handler(content_types = ['text'])
def answer_subject(message):
    if message.text == 'dosh':
        bot.send_message(message.chat.id, "Басталды 9455 жылы")
    elif message.text == 'wesh':
        bot.send_message(message.chat.id, "Басталды 7633 жылы")
    elif message.text == 'bash':
        bot.send_message(message.chat.id, "Басталды 5653 жылы")
    elif message.text == 'hash':
        bot.send_message(message.chat.id, "Басталды 5438 жылы")
    elif message.text == 'bysh':
        bot.send_message(message.chat.id, "Басталды 5634 жылы")


    '''

def answer(message):
    keyboard = types.ReplyKeyboardMarkup()
    
    
        


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




=======
@bot.message_handler(content_types=["text"])
def any_msg(message):
    keyboard = types.InlineKeyboardMarkup()
    if message.text=='привет':
        bot.send_message(message.chat.id, 'привет,как ваши дела?')
    elif message.text == "отлично" and 'хорошо':
        bot.send_message(message.chat.id, "Quanyshtymyn!!")
        bot.send_message(message.chat.id, 'Может вам понадобиться наши инлайн кнопки')
    if message.text == "пока нет":
        bot.send_message(message.chat.id, 'OK!!')
    if message.text == 'давайте':
        bot.send_message(message.chat.id, 'Вот!' )
    if message.text == 'открой мне гугл классрум':
        bot.send_message(message.chat.id, 'Открываю https://classroom.google.com нажмите на ссылку')
    url_button = types.InlineKeyboardButton(text=" k kaba kz",url='https://www.youtube.com/channel/UC_cBsck6NyqzSDaNEfOJ5HQ' )
    url_button2 = types.InlineKeyboardButton(text="ютуб",url='https://www.youtube.com' )
    url_button3 = types.InlineKeyboardButton(text="меня создал",url='https://vk.com/id289417861' )
    url_button4 = types.InlineKeyboardButton(text='classroom',url='https://classroom.google.com')
    keyboard.add(url_button,url_button2,url_button3,url_button4)
    if message.text == 'открой мне ютуб':
        bot.send_message(message.chat.id, 'Открываю https://www.youtube.com нажмите на ссылку')

# Инлайн-режим с непустым запросом
@bot.inline_handler(lambda query: len(query.query) > 0)
def query_text(query):
    kb = types.InlineKeyboardMarkup()
    # Добавляем колбэк-кнопку с содержимым "test"
    kb.add(types.InlineKeyboardButton(text="Нажми меня", callback_data="test"))
    results = []
    single_msg = types.InlineQueryResultArticle(
        id="1", title="Press me",
        input_message_content=types.InputTextMessageContent(message_text="Я – сообщение из инлайн-режима"),
        reply_markup=kb
    )
    results.append(single_msg)
    bot.answer_inline_query(query.id, results)


# В большинстве случаев целесообразно разбить этот хэндлер на несколько маленьких
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "test":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Пыщь")
    # Если сообщение из инлайн-режима
    elif call.inline_message_id:
        if call.data == "test":
            bot.edit_message_text(inline_message_id=call.inline_message_id, text="Бдыщь")
>>>>>>> b0ef45fcd462f8bb393bf75b53df980a7c929696

if __name__ == '__main__':
    bot.polling(none_stop=True)
