import telebot
import datetime
import requests

bot = telebot.TeleBot("6315993694:AAFqBhqI7ROH_MmD6JxDNGAcAXWqf66XfY4")

print("hello")


@bot.message_handler(commands=['time'])
def send_message(message):
    bot.reply_to(message, time_message())


@bot.message_handler(commands=['temp'])
def send_message(message):
    bot.reply_to(message, temp_message())


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

    message = "San Jose:".upper() + "\n" + SanJose_Date + "\n" + SanJose_Time + "\n\n" \
              + "Belfast:".upper() + "\n" + Belfast_Date + "\n" + Belfast_Time + "\n\n" \
              + "Rotterdam:".upper() + "\n" + Rotterdam_Date + "\n" + Rotterdam_Time + "\n" + "\n\n" \
              + "Tehran:".upper() + "\n" + Tehran_Date + "\n" + Tehran_Time + "\n" + "\n\n" \
              + "Auckland:".upper() + "\n" + Auckland_Date + "\n" + Auckland_Time

    return message


def temp_message():
    san_jose_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/san%20jose?unitGroup=metric&elements=datetimeEpoch%2Ctemp&include=current&key=CB93XCP3CPJN2SRCDKYZCP5TU&contentType=json"
    belfast_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/belfast?unitGroup=metric&elements=datetimeEpoch%2Ctemp&include=current&key=CB93XCP3CPJN2SRCDKYZCP5TU&contentType=json"
    rotterdam_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/rotterdam?unitGroup=metric&elements=datetimeEpoch%2Ctemp&include=current&key=CB93XCP3CPJN2SRCDKYZCP5TU&contentType=json"
    tehran_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/tehran?unitGroup=metric&elements=datetimeEpoch%2Ctemp&include=current&key=CB93XCP3CPJN2SRCDKYZCP5TU&contentType=json"
    auckland_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/auckland?unitGroup=metric&elements=datetimeEpoch%2Ctemp&include=current&key=CB93XCP3CPJN2SRCDKYZCP5TU&contentType=json"

    san_jose_data = requests.get(san_jose_url).json()
    belfast_data = requests.get(belfast_url).json()
    rotterdam_data = requests.get(rotterdam_url).json()
    tehran_data = requests.get(tehran_url).json()
    auckland_data = requests.get(auckland_url).json()

    san_jose_temp = str(san_jose_data["currentConditions"]["temp"])
    belfast_temp = str(belfast_data["currentConditions"]["temp"])
    rotterdam_temp = str(rotterdam_data["currentConditions"]["temp"])
    tehran_temp = str(tehran_data["currentConditions"]["temp"])
    auckland_temp = str(auckland_data["currentConditions"]["temp"])

    message = "San Jose:".upper() + "\n" + san_jose_temp + "\u00b0C" + "\n\n" \
              + "Belfast:".upper() + "\n" + belfast_temp + "\u00b0C" + "\n\n" \
              + "Rotterdam:".upper() + "\n" + rotterdam_temp + "\u00b0C" + "\n\n" \
              + "Tehran:".upper() + "\n" + tehran_temp + "\u00b0C" + "\n\n" \
              + "Auckland:".upper() + "\n" + auckland_temp + "\u00b0C"

    return message


bot.infinity_polling()
