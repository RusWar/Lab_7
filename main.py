import telebot
from telebot import types
import psycopg2

token = "5707665177:AAEsVg2fE_S6TRa6rwZZCttCrGJnmNj2sQU"
bot = telebot.TeleBot(token)
conn = psycopg2.connect(database="MTUSI_db", user="postgres", password="12345", host="localhost", port='5432')
cursor = conn.cursor()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Бот с информацией о расписании БИН2210.\n\nСписок команд:\n/menu -- выбрать неделю или день недели\n/week -- показать тип текущей недели\n/help -- вывод этого меню\n/mtuci -- ссылка на официальный сайт МТУСИ\n'
                                      '\nИ да, я Райн Гослинг из художественного фильма "Драйв"\n')


@bot.message_handler(commands=['menu'])
def menu_message(message):
    markup = types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton(text='Текущая неделя', callback_data='button1')
    button2 = telebot.types.InlineKeyboardButton(text='Следующая неделя', callback_data='button2')
    markup.row(button1, button2)
    button3 = telebot.types.InlineKeyboardButton(text='Понедельник', callback_data='button3')
    button4 = telebot.types.InlineKeyboardButton(text='Вторник', callback_data='button4')
    button5 = telebot.types.InlineKeyboardButton(text='Среда', callback_data='button5')
    button6 = telebot.types.InlineKeyboardButton(text='Четверг', callback_data='button6')
    button7 = telebot.types.InlineKeyboardButton(text='Пятница', callback_data='button7')
    button8 = telebot.types.InlineKeyboardButton(text='Суббота', callback_data='button8')
    markup.row(button3, button4, button5, button6, button7, button8)

    bot.send_message(message.chat.id, 'Выберите неделю или день недели...', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_function1(callback_obj):
    if callback_obj.data == 'button1':
        bot.send_message(callback_obj.from_user.id, 'Расписание на текущую неделю')
    elif callback_obj.data == 'button2':
        bot.send_message(callback_obj.from_user.id, 'Расписание на следующую неделю')

    elif callback_obj.data == 'button3':
        cursor.execute("SELECT * FROM bin2210 WHERE day = 'Понедельник'")
        record = list(cursor.fetchall())
        info = []
        for i in range(len(record)):
            add = record[i][1] + " " + record[i][2] + " " + record[i][3]
            info.append(add)
        bot.send_message(callback_obj.from_user.id, 'Расписание на понедельник:\n')
        for i in range(len(info)):
            bot.send_message(callback_obj.from_user.id, '' + info[i])

    elif callback_obj.data == 'button4':
        cursor.execute("SELECT * FROM bin2210 WHERE day = 'Вторник'")
        record = list(cursor.fetchall())
        info = []
        for i in range(len(record)):
            add = record[i][1] + " " + record[i][2] + " " + record[i][3]
            info.append(add)
        bot.send_message(callback_obj.from_user.id, 'Расписание на вторник')
        for i in range(len(info)):
            bot.send_message(callback_obj.from_user.id, '' + info[i])

    elif callback_obj.data == 'button5':
        cursor.execute("SELECT * FROM bin2210 WHERE day = 'Среда'")
        record = list(cursor.fetchall())
        info = []
        for i in range(len(record)):
            add = record[i][1] + " " + record[i][2] + " " + record[i][3]
            info.append(add)
        bot.send_message(callback_obj.from_user.id, 'Расписание на среду')
        for i in range(len(info)):
            bot.send_message(callback_obj.from_user.id, '' + info[i])

    elif callback_obj.data == 'button6':
        cursor.execute("SELECT * FROM bin2210 WHERE day = 'Четверг'")
        record = list(cursor.fetchall())
        info = []
        for i in range(len(record)):
            add = record[i][1] + " " + record[i][2] + " " + record[i][3]
            info.append(add)
        bot.send_message(callback_obj.from_user.id, 'Расписание на четверг')
        for i in range(len(info)):
            bot.send_message(callback_obj.from_user.id, '' + info[i])

    elif callback_obj.data == 'button7':
        cursor.execute("SELECT * FROM bin2210 WHERE day = 'Пятница'")
        record = list(cursor.fetchall())
        info = []
        for i in range(len(record)):
            add = record[i][1] + " " + record[i][2] + " " + record[i][3]
            info.append(add)
        bot.send_message(callback_obj.from_user.id, 'Расписание на пятницу')
        for i in range(len(info)):
            bot.send_message(callback_obj.from_user.id, '' + info[i])

    elif callback_obj.data == 'button8':

        cursor.execute("SELECT * FROM bin2210 WHERE day = 'Суббота'")
        record = list(cursor.fetchall())
        info = []
        for i in range(len(record)):
            add = record[i][1] + " " + record[i][2] + " " + record[i][3]
            info.append(add)
        bot.send_message(callback_obj.from_user.id, 'Расписание на субботу')
        for i in range(len(info)):
            bot.send_message(callback_obj.from_user.id, '' + info[i])

    bot.answer_callback_query(callback_query_id=callback_obj.id)


@bot.message_handler(commands=['mtuci'])
def mtuci_message(message):
    bot.send_message(message.chat.id, 'Официальный сайт МТУСИ: https://mtuci.ru/')


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Бот с информацией о расписании.\n\nСписок команд:\n/menu -- выбрать неделю или день недели\n/week -- показать тип текущей недели\n/help -- вывод этого меню\n/mtuci -- ссылка на официальный сайт МТУСИ\n')


@bot.message_handler(commands=['current_week'])
def current_week(message):
    bot.send_message(message.chat.id, 'Расписание на текущую неделю')


@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == '/mtuci':
        mtuci_message()
    elif message.text == '/menu':
        menu_message()
    elif message.text == '/help':
        help_message()
    else:
        bot.send_message(message.chat.id, 'Извините, я Вас не понял')

bot.infinity_polling()
