from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '100',
}
headers = {
    'Accepts': 'application/json',
    'Accepts-Encoding': 'deflate, gzip',
    'X-CMC_PRO_API_KEY': '43f6acbc-1136-4ee8-87bd-d17b1c6d82bd',
}

session = Session()
session.headers.update(headers)


def crypto_message():
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        crypto_mssg = ''
        for i in range(10):
            name = data['data'][i]['name']
            price = data['data'][i]['quote']['USD']['price']
            rounded_price = round(price, 3)
            percent_change_24h = round(data['data'][i]['quote']['USD']['percent_change_24h'], 1)
            crypto_mssg = crypto_mssg + '\n' f'{name}: {rounded_price} - 24h%: {percent_change_24h}'
        print(crypto_mssg)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    return crypto_mssg
