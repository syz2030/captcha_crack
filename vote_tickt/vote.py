# -*- coding:utf-8 -*-
import requests

headers = {
    'Host': 'v48bz.xiaodewl.com.cn',
    'Proxy-Connection': 'keep-alive',
    'Content-Length': '16',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Origin': 'http://v48bz.xiaodewl.com.cn',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; VOG-AL10 Build/HUAWEIVOG-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.143 Mobile Safari/537.36 MMWEBID/5117 MicroMessenger/7.0.17.1720(0x27001134) Process/tools WeChat/arm32 NetType/WIFI Language/zh_CN ABI/arm32',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie': 'PHPSESSID=eb5360b6d969a91d5704fdda5614e826',
}

url = 'http://v48bz.xiaodewl.com.cn/app/index.php?i=1&c=entry&do=listajax&m=haawei_vote'

data = {
    'hdid': '622',
    'p': '57338'
}

r = requests.post(url=url, headers=headers, data=data)

print(r.json())


