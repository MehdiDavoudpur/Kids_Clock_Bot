import telebot
import datetime

bot = telebot.TeleBot("6171477907:AAEna8FFur3jzZheD6AIBgBZFRNTu8qMUeM")

print("hello")


@bot.message_handler(commands=['times'])
def send_welcome(message):
    bot.reply_to(message, time_message())


def time_message():
    gmt_time = datetime.datetime.utcnow() + datetime.timedelta(hours=0)

    SanJose_time = gmt_time + datetime.timedelta(hours=-7)
    SanJose_Date = SanJose_time.strftime('%A')
    SanJose_Time = SanJose_time.strftime('%H:%M:%S')

    Belfast_time = gmt_time + datetime.timedelta(hours=1)
    Belfast_Date = Belfast_time.strftime('%A')
    Belfast_Time = Belfast_time.strftime('%H:%M:%S')

    Rotterdam_time = gmt_time + datetime.timedelta(hours=2)
    Rotterdam_Date = Rotterdam_time.strftime('%A')
    Rotterdam_Time = Rotterdam_time.strftime('%H:%M:%S')

    Tehran_time = gmt_time + datetime.timedelta(hours=3.5)
    Tehran_Date = Tehran_time.strftime('%A')
    Tehran_Time = Tehran_time.strftime('%H:%M:%S')

    Auckland_time = gmt_time + datetime.timedelta(hours=12)
    Auckland_Date = Auckland_time.strftime('%A')
    Auckland_Time = Auckland_time.strftime('%H:%M:%S')

    message = "San Jose" + "\n" + SanJose_Date + "\n" + SanJose_Time + "\n\n" + "Belfast" + "\n" + Belfast_Date + "\n" + Belfast_Time + "\n\n" + "Rotterdam" + "\n" + Rotterdam_Date + "\n" + Rotterdam_Time + "\n\n" + "Tehran" + "\n" + Tehran_Date + "\n" + Tehran_Time + "\n\n" + "Auckland" + "\n" + Auckland_Date + "\n" + Auckland_Time

    return message


bot.infinity_polling()
