import config
import telebot, requests
from telebot import types

bot = telebot.TeleBot(config.token)
# Neoбычный режим
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

if __name__ == '__main__':
    bot.polling(none_stop=True)
