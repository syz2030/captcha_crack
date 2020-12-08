# -*- coding:utf-8 -*-
import random
import re
import time
import base64
from hashlib import md5

import requests


class Login:
    # 破解验证和登录

    def __init__(self):
        self.headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                          '87.0.4280.66 Safari/537.36',
            'Accept': '*/*',
            # 'Origin': 'https://passport.stage.yunshanmeicai.com',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            # 'Referer': 'https://passport.stage.yunshanmeicai.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        self.appid = ''
        self.sample = ''
        self.data = ''
        self.c = '5fce3cf64HEMSwG7O7arufS3pzVARW2MoJa3i9O1'
        self.token = '6020E793FA3752A68A0D2B85FEF5091F439E165ADB40B7CC2CCEF541EA5550E30176A7D964BB8CAB7F50FDF23CF07' \
                     'F0F3965881D38A5CA0F1B78FC0E77163A06FBF34C5915CA412670CF06A57308C2F4'
        self.sid = ''
        self.y = ''
        self.x = ''

    def get_params(self):
        # 获取params参数
        '''
        addParams =
        url += (url.indexOf('?') == -1 ? '?': '&')
        url += encodeURIComponent(name) + '=' + encodeURIComponent(value)
        pass
        '''

    def get_index(self):
        # 获取ak和sample参数
        ak_url = 'https://passport.stage.yunshanmeicai.com/pc/site/index'
        ak_response = requests.get(url=ak_url, headers=self.headers)
        self.appid = re.findall(r"appId: \'(.*?)\',", ak_response.text)[0]
        sample_url = 'https://passport.yunshanmeicai.com/dist/scripts/process.min.js? [sm]'
        sample_response = requests.get(url=sample_url, headers=self.headers)
        self.sample = re.findall(r"i=\"(.*?)\"", sample_response.text)[0]
        print(self.appid, self.sample)

    def get_sid(self):
        # 获取sid和y值以及三张图片
        url = 'https://cap.dingxiang-inc.com/api/a'
        params = {
            'w': '300',
            'h': '150',
            's': '50',
            'ak': '85f04b56d0efac5cecb6fe15cca1439b',
            # 'c': '5fccd016N6RtGv2go0MgKAoSB3u96PqW5Dftccw1',
            'jsv': '1.4.5.1',
            'aid': 'dx' + '-' + str(int(time.time() * 1000)) + '-' + str(
                random.randint(10000000, 99999999)) + '-' + '1',
            'wp': '1',
            'de': '0',
            'uid': '',
            'lf': '0',
            'tpc': '',
            # 't': '792F9CBB39B9762A515B623F041127450D3F60628686677D2ABAE6C88BB938132A12C43581BBEB8D9923DC0CB3
            # A52050B775668C2F6B700DA89C26248E6B869DB083DE3B8E38377068492B3853E51C93',
            # '_r': '0.27547498369964885',
        }
        r = requests.get(url=url, headers=self.headers, params=params)

        print(r.json())
        return r.json()['sid'], r.json()["y"]

    def get_data(self):
        # 获取到data
        url = 'https://constid.dingxiang-inc.com/udid/c1?'
        param = '1714#X8m8KVRy8B0KKKIbfd9LrBVL06U40hFJdaN4XBd45NFbnbqjF8F4dyZ4BRNj0CN4dzN4BH94rVU4dOd4XKILz/UKHOV' \
                '40yI4Xwd48bqb0hFJnBoYXX0yw4Lu74LmMvUkrXIXYZ6c9GE+SnNgmXXI8XojUMuR+zXz3MbRm8m7uV2su7rDtJpWEGpGYK4n9B' \
                'Ld4NlsNw0ekYwdNRedYFLDKiLd+S0k6jESbdMfUnHdYHwgpVQlhMpxEwwzhYCS9tCfbdJxJRevpkHdp5pehB4xhtpeq5HdiDoWqg' \
                'Qs7dCS9BLDUmC5KZ4f6FWlY9osPn0zhYCS9tCfu2fXj1fSU1CNkXWGUAalJXWXmoKeMpRJ7rrXjcSZYV/vOm7Om8yxj2miY8X' \
                '1udgWFr82YrX1oWDcoRUEY2XPPxKWw0eUdX2X3mPG4bqtg9TgyOxI4pYHirgZXXBCS0RQYluLAegaMO4quqrUXXyz/w2JvXybmR' \
                '/FXXxiuX88YaacmAu43XX1RtZ8WyC738X1rBYjSOpl3rXPnNcpOYIGImIXmEZKDsziGM8XmerAfXnfXM/XuvdxAeEYSvYew+wXob' \
                'kQEKl1bOYturXSTrb8ayagW1W18Xva8X81XznwIua1/2mna2fmHNuE/TW1mCVI/r8rWmWXvhzT3EyoiWdhVQutyJyUoc1lRIdhV' \
                'QutyJcFVMiMWVBt3D1TItyfXXomI9IjXW3LKcUs1MyXYBU70kGwqGJ20+iV1rXss6ZzJYVVk6xzJ65kXXQl3uSq8/cTIcyssT2X' \
                'mSzCL+KaxmVXjSzp8blqplFi/lFntdEqPrXFu6nTI2ye1EgWiC3x1tgZX8X1KVIjKBG4XrX17ZsWr5pTX2Xv9kkY5ZeedpG4mXXe' \
                '8XyhijvRI6Cx89nj/axHXu9/F3cRsEo2aXcRaXC4mX9RkTxaiDQz/cZ/u8=='
        headers = self.headers
        headers['param'] = param
        r = requests.get(url=url, headers=headers)
        print(r.content.decode())
        return r.json()['data']

    def get_token(self):
        # 完成验证码验证获取token
        url = 'https://cap.dingxiang-inc.com/api/v1'
        self.sid, self.y = self.get_sid()
        self.data = self.get_data()
        data = {
            # 'ac': '1786#X8XnXTgBGWLTuY3YXXOXR37cJDS3X3zcLHvwWBZRsIeigMuR/BFhIdUluvUt/BnToxiT3c3T3
            # lxTVxsig9Pi/MvwyWShoz1TbI2TgBF8/x3/LuURgBZt3x3wVZUTIJDcm8X18AbnULS+mrXmZXWXmIBFwggnX
            # X89ZR/VY8XEMSP/2nLuV7P8yZs3VIh1AZJRCxUjy5HXrWhXybJ8EOU1yXIXusO1JbbTqoqmCgjfidhWUiPlz
            # fYfY2Xi5JPqKUzLKfsC58oXYpPCliBCnF3B5J3sXXeCq/lp5HGM/KPCY2XQ5Jc+ZpuEqJLCKrhyNBwoOnRgv
            # UwkbUMgsFwkH38omXMVhEMIP3SyDv8I4ZQljXXpfAchgDyxh+MRf/chRw/nXMr6UMuDutrt3rZa+myPY22Pi
            # cTHvh9KY8aX/CrV/2fXXR8sXYdCq6x25WdxiUPqmiRkBUMyCF2yGZ0VGP2oBZQgTY23jPTis32WhCTWBnMgN
            # NSTXXEd9GNoQ7eD9m3XYsHD0JqdNbHV38XnQbJbGGHG9B8TXXEd9Gd8Q90Dbm3XYsHD0H1d0ZHV38XnQbJbg
            # e4g9B8TXXEd9GdwQGdDbm3XYsHD04hdD4HV38XnQbJbbkJK9B8TXXEd9Gd6QdGDbm3XYsHDd4JdFbHV38XnQ
            # bH4psHr9B8TXXEd9bdOQqjDbm3XYsHDdkldr4HV38XnQbH4NG4Y9B8TXXEd9bdWQ2FDbm3XYsHDd4NdMZHV3
            # 8XnQbH4deWy9B8TXXEd9bdHQgDDbm3XYsHDdJYdv4HV38XnQbH45kH19B8TXXEd9bdEQ2kDbm3XYsHDdJUdx
            # QHV38XnQbH47sWP9B8TXXEd9bdcQVHDbm3XYsHDdJ+dtZH/38XnQbH4qsHn9b8TXXEd9bdpQKLD9m3XYsHD
            # dWKdiZH/38XnQbH4gs4S9b8TXXEd9bdTQgzD9m3XYsHDdHidi4H/38XnQbH4VGJv9b8TXXEd9bd/QKeD9m3
            # XYsHDdH6d+QH/38XnQbH49eHe9b8TXXEd9BdDQN0D9m3XYsHDBkEdGZH/38XnQbHbNk4I9b8TXXEd9BNqQg
            # dD9m3XYsHDB4pds4H/38XnQbHb0sJZ9b8TXXEd9Bd4QgGD9m3XYsHDBkqdjQH/38XnQbHbdG4p9b8TXXEd9
            # BdrQ5GD9m3XYsHDBJ1deQH/38XnQbHb5eHF9b8TXXEd9BdLQgBD9m3XYsHDBJhdsbH/38XnQbHb7e409b8T
            # XXEd9BdzQbjDoM3XYsHDBWEd3ZJR38XnQbHbqk4297ITXXEd9BdiQGjDyM3XYsHDBJpdV4JR38XnQbHbwsH
            # 97ITXXEd9BdQQBPDyM3XYsHDBWqd34JR38XnQbHbGGWM97ITXXEd9BdMQ9PDyM3XYsHDBHUdW4JR38XnQbH
            # bbkJT97ITXXEd9BV6QGPDyM3XYsHDP4pdVQJR38XnQbW4dsHh97ITXXEd9MdJQMsDyM3XYsHDP4KdIQJR38X
            # nQbW45s4h97ITXXEd9MdmQdsDyM3XYsHDPJidyQJR38XnQbW4GsJt97ITXXEd9Md2QbFDyM3XYsHDF4AdVbJ
            # R38XnQbWbNGHw97ITXXEd9wdWQMFDyM3XYsHDFJEdIbJR38XnQbWbGk4R97IiXX27p9JnM//12xJnMr/=',
            'ak': self.appid,
            'c': self.data,
            'uid': '',
            'jsv': '1.4.5.1',
            'sid': self.sid,
            'aid': 'dx' + '-' + str(int(time.time() * 1000)) + '-' + str(
                random.randint(10000000, 99999999)) + '-' + '1',
            'x': '207',
            'y': str(self.y)
        }
        print(data)
        r = requests.post(url=url, headers=self.headers, data=data)
        print(r.content.decode())

    def login(self, phone, pwd):
        login_url = 'https://passport.yunshanmeicai.com/pc/site/index'
        data = {
            "bp": "Win32",
            "credential": f"{{captcha={self.token + ':' + self.c}&password={pwd}&phone={phone}&type=password}}",
            "device_id": "41b27fa0a0b291156e406cab091bc6d0",
            "os": "Windows 10",
            "rs": "1920,1080",  # 分辨率
            "ts": str(int(time.time() * 1000)),
            "ua": str(self.headers['User-Agent']),
        }
        # 获取登录用的sign参数
        sample = self.sample
        st = '{' + '&'.join([k + '=' + v for k, v in data.items()]) + '}'
        sign = md5(base64.encodebytes((st + sample).encode())).hexdigest()
        data['sign'] = sign
        data['credential'] = {
            'phone': phone,
            'password': pwd,
            'captcha': self.token + ':' + self.c,
            'type': 'password',
        }
        index_response = requests.post(url=login_url, headers=self.headers, data=data)
        if index_response.status_code == 200:
            cookies = index_response.cookies
            return cookies


if __name__ == '__main__':
    t = Login()
    t.get_index()

''''
ua
ty

101100101011111
101100100110111
000000001101000

101100101011111
101100100110011
000000001101100

剩余三个参数破解
ac、params、x
ac和params同类、x距离
'''
