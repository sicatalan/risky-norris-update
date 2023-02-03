import requests
from secrets import acces_key


def main():
    

    function = 'TIME_SERIES_INTRADAY_EXTENDED'
    symbol = 'IBM'
    interval = '60min'
    slice = 'year1month1'
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={0}'.format(acces_key)
    api_result = requests.get(url)
    api_response = api_result.json()

    print(api_response)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')