# -*- coding:utf-8 -*-
import execjs
import requests
import json
from hashlib import md5


def get_toekn():
    with open('index.js', 'r', encoding='utf-8') as f:
        js = f.read()
    ctx = execjs.compile(js)
    token = ctx.call('fx')
    return token

url = 'https://api.yangkeduo.com/api/jinbao/h5_weak_auth/goods/query_goods_detail_and_sku'

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-length': '1047',
    'content-type': 'application/json; charset=UTF-8',
    'origin': 'https://youhui.pinduoduo.com',
    'pragma': 'no-cache',
    'referer': 'https://youhui.pinduoduo.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
}


data = {"goodsId": "115389836260", "goodsIds": ["115389836260"], "goodsSign": "JQ0zz2x5d2", "pid": None,
        "antiContent": get_toekn(),
        "anti_content": get_toekn()}

r = requests.post(url=url, headers=headers, data=json.dumps(data))

print(r.json())


