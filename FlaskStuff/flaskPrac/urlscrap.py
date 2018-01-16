import requests
import time

s = requests.Session()
for coin in coin_list:
    url = 'https://bittrex.com/Api/v2.0/pub/market/GetTicks?marketName=BTC-'+ coin + '&tickInterval=oneMin'
    try:
        balance = api.getbalance("BTC")
        time.sleep(1)
    except Exception as e:
        app_log.critical(e)
        return
        data_array = []
        page = s.get(url)
        print ("")
        time.sleep(1)
        print(BOT_NAME + ":Buying: Got the data.")
        page_response = page.text
        data = json.loads(page_response)
        coin_data = process_1_data(data)
        created_at = get_time()
        name = coin
        cur_price = float(data['result'][-1]['C'])
