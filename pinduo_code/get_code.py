# -*- coding:utf-8 -*-
import execjs
import requests
import json
from hashlib import md5
import js2py
from gen_token import js

def get_toekn():
    ctx = execjs.compile(js)
    print(ctx.call(''))

# get_toekn()




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

token = '0aoAfxnUXytoY9dVzr-vwmiCEh4t4bkkQX8x__yt3FsHvET4jy7XHFXpAZYU3_fDW14hKE5cVDVr2YJM9c6kaC9aZAE3fVSL4cnpkBw60vJ0suShz1Mve7hD-xLd7vkeykAD7-OOtagDzx9mxwpgrqPVsl9_b_fOcHbf6_KBRKUg9vV837lCgDd5qa4tfxVn0DV9c9kD_TzJmKG9HBgBq07feTprwjTC00l-AR04_S_E3hOxG_uSUl2S9dW12GFv2YqteUuz9LcqQdHOuRVbaFj6mHeEVyTWJCQylRZjqx7EZLZ_vDe9TUOTMsMr54DQhzoqnE48JOUIDKJFfe1PioSO2qGNxG6SV_RHVdIHNrI3ts-yyMUELdOa-ow521eqitsASc73ey1tfsGQUrkRL6UqUc1j87yRqe2bmIirNMh_h6u0ROmv4xpYgfb0e1HVZRuiM3c'

data = {"goodsId": "115389836260", "goodsIds": ["115389836260"], "goodsSign": "JQ0zz2x5d2", "pid": None,
        "antiContent": str(token),
        "anti_content": str(token)}

r = requests.post(url=url, headers=headers, data=json.dumps(data))

print(r.json())


