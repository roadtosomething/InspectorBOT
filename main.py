import telebot
from time import sleep

bot = telebot.TeleBot('5530656760:AAGAgKuFsVqZlneTqcPmy-z2u3VtlUlHHP4')
lang = 'ru'

@bot.message_handler()
def get_text_message(message):
    str = " "
    targetText = message.text.lower()
    print(targetText)
    trigerMikova = ["@diamikova","затян","обработай","проставь","смени","PKO_0000_0208",'свяжи','связа','формир','синхронизируй']
    trigerTrukhacheva = ["@Elenka_Evgen","смени","проставь","PKO_0000_0208"]
    trigerPokholkov = ["@Krasnoff_YT","обработай","затян",'свяжи','синхронизируй']
    trigerLamskov = ["@lamskoff","затян","обработай",'свяжи','связа','формир']
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
    if ("@" in str):
        bot.send_message(chat_id=message.chat.id, reply_to_message_id=message.id, text= str)
while True:
    try:
        bot.polling(none_stop=True,interval=0)
    except Exception as _ex:
        print(_ex)
        sleep(5)