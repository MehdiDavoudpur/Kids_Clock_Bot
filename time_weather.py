import datetime
import requests

# urls
SanJose_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/san%20jose?unitGroup=metric&elements=temp%2Csunrise%2Csunset%2Cconditions&include=current&key=CB93XCP3CPJN2SRCDKYZCP5TU&contentType=json"
Belfast_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/belfast?unitGroup=metric&elements=temp%2Csunrise%2Csunset%2Cconditions&include=current&key=CB93XCP3CPJN2SRCDKYZCP5TU&contentType=json"
Rotterdam_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/rotterdam?unitGroup=metric&elements=temp%2Csunrise%2Csunset%2Cconditions&include=current&key=CB93XCP3CPJN2SRCDKYZCP5TU&contentType=json"
Tehran_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/tehran?unitGroup=metric&elements=temp%2Csunrise%2Csunset%2Cconditions&include=current&key=CB93XCP3CPJN2SRCDKYZCP5TU&contentType=json"
Auckland_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/auckland?unitGroup=metric&elements=temp%2Csunrise%2Csunset%2Cconditions&include=current&key=CB93XCP3CPJN2SRCDKYZCP5TU&contentType=json"

location_list = ["San Jose".upper(), "Belfast".upper(), "Rotterdam".upper(), "Tehran".upper(), "Auckland".upper()]

url_list = [SanJose_url, Belfast_url, Rotterdam_url, Tehran_url, Auckland_url]


def time_weather_message():
    # create data_list that contains json data type of: [temp, cond, sunrise, sunset].
    # this is outer of below functions because of its usage in both of them
    data_list = []
    for url in url_list:
        data_list.append(requests.get(url).json())

    timeOffset_list = []
    for data in data_list:
        timeOffset_list.append(data['tzoffset'])

    print(timeOffset_list)

    gmt_time = datetime.datetime.utcnow() + datetime.timedelta(hours=0)

    #   create date_list & time_list from GMT Time & offset times
    date_list = []
    time_list = []
    for offset in timeOffset_list:
        date_list.append((gmt_time + datetime.timedelta(hours=offset)).strftime('%A'))
        time_list.append((gmt_time + datetime.timedelta(hours=offset)).strftime('%H:%M:%S'))

    #   create sunrise_list & sunset_list from data_list
    SunRise_list = []
    SunSet_list = []
    for sun in data_list:
        SunRise_list.append(sun["currentConditions"]["sunrise"])
        SunSet_list.append(sun["currentConditions"]["sunset"])

    temp_list = []
    cond_list = []
    message = ""
    for i in range(5):
        temp_list.append(str(data_list[i]["currentConditions"]["temp"]))
        cond_list.append(data_list[i]["currentConditions"]["conditions"])
        message = message + location_list[i] + "\n" + date_list[i] + " - " + time_list[i] + "\nSunRise: " + \
                  SunRise_list[i] + "\nSunSet: " + SunSet_list[i] + "\n" + temp_list[i] + "\u00b0C\n" + cond_list[
                      i] + "\n\n"

    return message


print(time_weather_message(), "\n\n")
