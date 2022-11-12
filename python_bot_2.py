import telebot
import requests
from bs4 import BeautifulSoup as bs
import lxml


# Создаем экземпляр бота ( в ковычках введите HTTP API вышего бота (его вам даст BotFather))
bot = telebot.TeleBot('')
def get_wiki(s):
    #Сохраняем строку для поиска
    print(s)
    s1=''
    for i in s:
        if ord(i)<1072:
            s1+=chr(ord(i)+32)
        else:
            s1+=i
    url = "https://ru.wiktionary.org/wiki/"+s1
    print(url)
    #ищем html код
    r = requests.get(url)

    #записываем  html код в суп
    soup=bs(r.text,'lxml')
    #достаём из html кода весь текст
    text=soup.get_text()
    #создаём массив для строк
    lines=[]
    #проходим весь текст
    i=0
    while i<len(text):
        #каждая новая строка изначально пустая
        line=''
        #заполняем каждую строку до знака переноса строки или до конца файла
        while text[i]!='\n' and i<len(text):
            #прибавляем к строке новый символ
            line+=text[i]
            #увеличиваем индекс символа из текста
            i+=1
            #проверяем что строка не пустая
        if line!='' and line!='Производное:\xa0??.' and line[:42]!='Встречается также устар. вариант ударения:':
            #добавляем строку в массив
            lines.append(line)
        if (line=='Произношение' or line=='Произношение[править]') and len(lines)>3:
            break
        #увеличиваем индекс i чтобы пропустить перенос строки
        i+=1
    if lines[6]=='В настоящий момент текст на данной странице отсутствует.Вы можете найти упоминание данного названия в других статьях или создать страницу с таким названием.'or 'Недопустимое название — Викисловарь'==lines[0]:
        return 'Увы, на вики словаре нет страницы для этого слова или ваше слово имеет недопустимые для поиска символы. Поиск вёлся по адресу:\n'+url
    # Создаём переменные для хранение инфы
    razbor=lines[len(lines)-2]
    har=lines[len(lines)-3]
    slogs=lines[len(lines)-4]
    print(lines)
    out='Подробная информация о слове '+s+':\n'+slogs+'\n'+razbor+'\n'+har+'\n\nДля получения более подробной информации предлагаем Вам посетить источник:\n'+url
    return (out)
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wiktionary')
# Функция обрабатывающая команду /info
@bot.message_handler(commands=["info"])
def start(m, res=False):
    mes='Вся информация берётся из ru.Wiktionary.com.\n\nУвы, не получается вывести таблицы падежей и времён в должном виде, по этому их нет.\n\nЕсли информации по слову не нашлось, значит её нет на викисловаре.\n\nПо всем вопросам пишите @Noskov_Ilja'
    bot.send_message(m.chat.id, mes)
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, get_wiki(message.text))

# Запускаем бота
bot.polling(none_stop=True, interval=0)
