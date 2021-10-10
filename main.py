import requests as requests

import requests as requests
class Wrapper:
    def __init__(self, totalcount1):
        self.totalcount1 = totalcount1

    def get_news(self, coin_name):
        for i in range(len(coin_name)):
            if coin_name[i] == ' ' or coin_name[i] == '.':
             coin_name = coin_name.replace(' ', '-')
             coin_name = coin_name.replace('.', '-')

        result_list = []
        tc = self.totalcount1
        while True:
            url_api = f'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit={tc}&sortBy=market_cap&sortType=desc&convert=USD&cryptoType=all&tagType=all&audited=false'
            responce = requests.get(url=url_api)
            data = responce.json()
            for i in range(0, tc):
                result_list.append({
                    'id': data['data']['cryptoCurrencyList'][i]['id'],
                    'name': data['data']['cryptoCurrencyList'][i]['name']
                })
            print(result_list)
            for i in range(0, tc):
                if 'name' == 'Bitcoin' in result_list:
                    print(result_list.get('id'))
            coin_id = 0
            for i in range(len(result_list)):
                if result_list[i]['name'] == coin_name.lower().title():
                    coin_id = result_list[i]['id']
            urls = f'https://api.coinmarketcap.com/content/v3/news?coins={coin_id}'
            res = requests.get(url=urls)
            data_news = res.json()
            data_news_json = []
            for i in range(0, len(data_news['data'])):
                data_news_json.append({
                    'News title': data_news['data'][i]['meta']['title'],
                    'Text': data_news['data'][i]['meta']['subtitle']
                })
            return data_news_json

limit = int(input("Enter the limit:")) #insert the limit for example 20

andd = Wrapper(limit)

print(andd.get_news("bitcoin"))