import requests
from bs4 import BeautifulSoup
import json

def get_ithome_hot():
    url = 'https://www.ithome.com/block/rank.html'  # 替换为你的URL
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0',

    }
    response = requests.get(url,headers=headers)

    if response:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'lxml')

        dayhot = soup.select("#d-1>li>a")
        dayhot = [{"word": item.get_text(), "url": item.get("href")} for item in dayhot]

        weekhot = soup.select("#d-2>li>a")
        weekhot = [{"word": item.get_text(), "url": item.get("href")} for item in weekhot]

        monthhot = soup.select("#d-3>li>a")
        monthhot = [{"word": item.get_text(), "url": item.get("href")} for item in monthhot]

        new_data = {
            "dayhot": dayhot,
            "weekhot": weekhot,
            "monthhot": monthhot
        }
        print(new_data)
        return new_data

    else:
        print("请求失败")
