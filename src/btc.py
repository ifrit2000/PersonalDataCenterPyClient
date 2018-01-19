# -*- coding: UTF-8 -*-

import json
import os
import time

import urllib3
from urllib3.exceptions import InsecureRequestWarning

http_pool = urllib3.PoolManager()
urllib3.disable_warnings(InsecureRequestWarning)


def get_k_line(coin_name):
    url = 'api.huobipro.com/market/history/kline?symbol=%susdt&size=1&period=1min' % coin_name
    response = http_pool.request("GET", url)
    return json.loads(response.data)


def get_cur_price(coin_name):
    res = get_k_line(coin_name)
    return res["data"][0]["close"]


def read_config_file(config_file_name):
    file_object = open(config_file_name)
    try:
        all_the_text = file_object.read()
    finally:
        file_object.close()
    return json.loads(all_the_text)


def get_exchange_rate():
    url = "https://api-otc.huobi.pro/v1/otc/trade/list/public?coinId=2&tradeType=1&currentPage=1&online=1&range=0"
    response = http_pool.request("GET", url)
    return json.loads(response.data)['data'][0]['price']


def main():
    config = read_config_file("position.json")
    hold_usdt = config["holdUsdt"]

    hold_coins = config["hold"]

    refresh = config["refresh"]

    while (True):
        usdt_to_cny = get_exchange_rate()

        total_usdt = 0
        price_list = list()
        try:
            for coin in hold_coins:
                price = get_cur_price(coin["name"])
                price_list.append(coin["name"] + " :" + str(round(price, 2)))
                usdt = price * coin["position"]
                total_usdt = total_usdt + usdt
        except json.decoder.JSONDecodeError:
            continue

        os.system('cls')
        print("汇率:%s" % str(usdt_to_cny))
        for p in price_list:
            print(p)

        print("合计信息:")
        print("usdt :" + str(round(total_usdt, 2)))
        print("cny  :" + str(round((total_usdt + hold_usdt) * usdt_to_cny, 2)))
        print("time :" + str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
        time.sleep(refresh)


if __name__ == '__main__':
    main()
