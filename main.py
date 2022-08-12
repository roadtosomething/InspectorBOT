import telebot
from telebot import types
from time import sleep
import datetime
import yadisk
import config as conf
from tagDict import dict
import pandas as pd
#
bot = telebot.TeleBot(conf.tokenBot)
lang = 'ru'
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
start_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn = types.KeyboardButton("Выгрузить ДЗМ")
btn2 = types.KeyboardButton("Выгрузить ДЗМ для меня")
markup.add(btn,btn2)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Готов выгружать и показывать!", reply_markup=markup)
@bot.message_handler()
def get_text_message(message):
    str = " "
    targetText = message.text.lower()
    print(targetText)
    trigerMikova = ["@diamikova","тян","обработай","проставь","смени","PKO_0000_0208",'свяжи','связа','формир','синхронизируй']
    trigerTrukhacheva = ["@Elenka_Evgen","смени","проставь","PKO_0000_0208"]
    trigerPokholkov = ["@Krasnoff_YT","обработай","тян",'свяжи','синхронизируй']
    trigerLamskov = ["@lamskoff","тян","обработай",'свяжи','связа','формир']
    trigerGudkov = ["@Georgiy_Gudkov","ошибка","смени","проставь",'поправь','пг_ик_4004','посмотри','убери','смп']
    trigerGilev = ["@Smiiiita","эа2020_ик_10127","спек","спецификаци",'замени']
    trigerVoronin = ["@jlmdie","эа2020_ик_10127","спек","спецификаци",'sid','сид']
    trigerLuchnikov = ['@Melogor','Сумма контракта превышает предложение участника','apk_0000_0614']
    trigerMaksimov  = ['@MaksimovVM','Сумма контракта превышает предложение участника','apk_0000_0614']
    trigerSedov = ["@mis_sed",'финансирован']

    def tagName(triger):
        for value in triger:
            if value in targetText:
                str = triger[0]+" "
                break
            else:
                str = ''
        return str

    if "test" in targetText:
        print(message.chat.id)
    if 'выгрузить дзм' in targetText:
        cols = [3, 11, 13,14]
        file_name = 'data.xlsx'
        try:
            y = yadisk.YaDisk(token=conf.tokenYad)
        except Exception:
            bot.send_message(message.chat.id,'Кто-то недавно обновил файл, попробуй через пару секунд выгрузить, а то яндекс тормозит', reply_markup=markup)
        if y.check_token():
            y.download('/ДЗМ.xlsx', file_name)
        print("Dowload done...")
        i = 0
        t = datetime.date.today()
        while True:
            try:
                t = datetime.date.fromordinal(t.toordinal() - i)
                df = pd.read_excel(file_name, sheet_name=t.__format__('%d.%m'), usecols=cols)
                break
            except ValueError:
                i = i + 1
        print('DFForming done...')
        df2 = df.fillna("Пустое значение")
        df3 = df2[(df2['Способ решения'] == 'Пустое значение') & (df2['Ответственный ТП3']!='MorozovaAV')][['Код инцидента','Ответственный ТП3','Решение']]
        df3.sort_values(by='Ответственный ТП3')
        dataframe_list = df3[df3['Решение']=='Пустое значение'][['Код инцидента','Ответственный ТП3']].values.tolist()
        print('ListInformationForming done...')
        strMessage = "Просьба заполнить ДЗМ\nhttps://disk.yandex.ru/i/rCzzuoBHTJyYFQ\n" \
              "Следующих специалистов:\n"
        print('Begin Formating string message')
        for item in dataframe_list:
            strMessage = strMessage + item[0] + ' ' + dict[item[1]] + '\n'
        if ('для меня') in targetText:
            print('Message send for you')
            bot.send_message(message.chat.id,strMessage)
        else:
            print('Message send')
            bot.send_message(conf.chatVEP,strMessage)


    if "/contract/" in targetText:
        if 'sid' not in targetText or 'сид' not in targetText:
            str += tagName(trigerMikova)
            str += tagName(trigerTrukhacheva)
        str += tagName(trigerPokholkov)
        str += tagName(trigerLuchnikov)
        str += tagName(trigerMaksimov)
        str += tagName(trigerGilev)
        str += tagName(trigerVoronin)
    if "/plan-purchase-schedules/" in targetText:
        str += tagName(trigerLamskov)
        str += tagName(trigerMikova)
        str += tagName(trigerGudkov)
        if 'не удалось найти информацию о финансировании' not in targetText:
            str += tagName(trigerSedov)
    if "/lots2020/" in targetText:
        str += tagName(trigerGudkov)
        str += tagName(trigerSedov)
        str += tagName(trigerGilev)
        str += tagName(trigerVoronin)
    if "/definition-supplier/" in targetText:
        str +=tagName(trigerMikova)
        str +=tagName(trigerLamskov)
        str +=tagName(trigerGudkov)
    print(str)
    if 'Просьба заполнить ДЗМ' not in str:
        if (message.chat.id == -1001526837008):
            if ("@" in str):
                bot.send_message(chat_id=message.chat.id, reply_to_message_id=message.id, text= str)
while True:
    try:
        bot.polling(none_stop=True,interval=0)
    except Exception as _ex:
        print(_ex)
        sleep(1)