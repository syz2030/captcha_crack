# -*- coding:utf-8 -*-
import execjs
import requests
import json
from hashlib import md5
import js2py


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

token = requests.get(url='http://127.0.0.1:8000/get_anti_content').json()["anti_result"]
# token = '0aoAfxnUGNGoY9mavX6fYW7oSYO3lzDibzG7ewkz1owadGp__LfVwanmjMkElldYugRaqRQ0PJloKHALrnLhGl2Joa4lmxQaiKoJL1ODWGBJX1dkznLJmpc7lAjcRCi7oxfax5qW2B9pxTTcfeiP44CT9Z2bJbgtlla2HFJKFGPwlfKIVP-tkl_25oFzKz-89AMlITWKZZdxqBCYDShHir6NGw46-4ESnJTDPflCS8w7vdvA185Kp-3MQ1E45wkGFDVJad1qsk5cd3juSx-Azy8jKdi2Hq3mvCPNtSxveOW1VOsymxzib-tiGTO1FdmjDuJUNRDvO2ZU33pF58dtDqUMRNlWF8iuumQRMaSnT'
# token = '0aoAfxn5HycYY9dw1R69_1aC9dGK4D_CsZUtQVha-l7tt9jFttzCZ4fMtqTjfLdvKxlLuCYqVh9zR9Bh2fhoFZna2eKulRwY7Wy5kE2S0uCSvjUoj6ACeuQqV7rDZ6TSdODcsDoKJzO0IjWGWo96uyzk1oG4sBYdxmVCHm3kBiw2-yZAtmAtp7k186DmtWrhDIJKoeLNDvOwu2v3M4hv1SS0cgbzZyL_v7F-NA-jmC31vX5pjRZz1KMw6fO95agzkt0LcOo6i9e_U7hj6dm_CUVF6565hRteKDhXSuwjRnrAP4_dPm0C2uSMz6VGe8PsvqEGIuOo-PZzUsmoclEdoI8d2sK5vSLIOE2jVEulQjvo6udZWftLOPHJ3eIzGCW1PRfjo8inXzjevV0I9_5TLaFN9ZWb6U-9VsAKK7KgHrC0QmhQYxhQCboF1JgQVWw_VLVmvGtOp2NqL9X3hZzowZAr4dhYRYv0s4q3mRqX8FpMQBblj3xW2IlbDuoUDxp0_QePC3ZVF3dHWdFdA-3ihNY2bvGd0lh9D1PyYRGYNFHiO3mW93OzDBunPz84g3cw3lRgvl049'
print(token)
print(len(token))
data = {"goodsId": "115389836260", "goodsIds": ["115389836260"], "goodsSign": "JQ0zz2x5d2", "pid": None,
        "antiContent": str(token),
        "anti_content": str(token)}
s = "0aoAfxn5DNGoY9dCfXlpStl0VvcDgBp_x3b_xj4OvkGh3dOD_AbnFmp-hD_OX7B1znyu8famt5CJl9CZ0CJ4PJcqISJc6wYN9Gi9mG5JiQ5QvbXFZpbkM347re5iekr4Nbe7JPW1wR2HRpKNvVAM6jt_eRJTE_earZAPLcQ_wQrBOFneBR4JVma3mL3s-DnlLjA8yy_ye08MD3IiBLDLMXa_Kj8vBFFl6YRFEr59jHKI2nU-pSUZa1BFSFyDBZgzQh0jTKCKt67pdkeeFfnTNVBG9IPwn_j1z6TY9jL-iA5TD00pyqQS31KTf9SZjRrc9OjZY404Uo0gD4w2CnHfg6BNqyzeIdOO3AkZ4CPCrwzhIZqhT9rOrM921H8AwfUME48-BSw2_1BDUgsEy4C0w1JWyW0wX7Qr7EMwxO-nhprE1840jOveJj6B6FvcyoQ5m89VCWl3niDF8Q2k1Fd7smGAqvE3CotEEudxb-5bAvW1f3nzo"
print(len(s))

r = requests.post(url=url, headers=headers, data=json.dumps(data))

print(r.json())
