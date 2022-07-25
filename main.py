import telebot


bot = telebot.TeleBot('5530656760:AAGAgKuFsVqZlneTqcPmy-z2u3VtlUlHHP4')
lang = 'ru'



@bot.message_handler(content_types=['text'])
def get_text_message(message):
    str = " "
    targetText = message.text.lower()
    trigerMikova = ["@diamikova","затян","обработай","проставь","смени","PKO_0000_0208",'свяжи','связа','формир','синхронизируй']
    trigerTrukhacheva = ["@Elenka_Evgen","смени","проставь","PKO_0000_0208"]
    trigerPokholkov = ["@Krasnoff_YT","обработай","затян",'свяжи','синхронизируй']
    trigerLamskov = ["@lamskoff","затян","обработай",'свяжи','связа','формир']
    trigerGudkov = ["@Georgiy_Gudkov","ошибка","смени","проставь",'поправь','ПГ_ИК_4004','посмотри']
    trigerGilev = ["@Smiiiita","ЭА2020_ИК_10127","спек","спецификаци",'замени']
    trigerVoronin = ["@jlmdie","ЭА2020_ИК_10127","спек","спецификаци",'sid','сид']
    trigerLuchnikov = ['@Melogor','Сумма контракта превышает предложение участника']
    trigerMaksimov  = ['@MaksimovVM','Сумма контракта превышает предложение участника']
    trigerSedov = ["@mis_sed",'финансирован']

    def tagName(triger):
        for value in triger:
            if value in targetText:
                str = triger[0]+" "
                break
            else:
                str=''
        return str


    if "/contract/" in targetText:
        if ((" сид" not in targetText) and (' sid ' not in targetText)):
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
    try:
        print(str)
    except:
        print("Не найдено слово-триггер")
    if ("@" in str):
        bot.send_message(chat_id=message.chat.id, reply_to_message_id=message.id, text= str)

bot.polling(none_stop=True, interval=0)
