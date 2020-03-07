#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

import requests

price_url = "http://user.mbaex.com/real/market.html?symbol=14&buysellcount=100&successcount=100&coinName=USD&random=76"

# http://user.mbaex.com/trade/coin.html?coinType=7&tradeType=0


response = requests.get(price_url)

print(response.content)

content = json.loads(response.content)

p_high = content["high"]

p_low = content["low"]

print(p_high)