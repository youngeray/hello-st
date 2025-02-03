import requests
from bs4 import BeautifulSoup
import json
import streamlit as st

def get_bbczw_hot():
    url = st.secrets['bbczw_url']  # 替换为你的URL
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

        dayhot = soup.select(".promo-text a")
        dayhot = [{"word": item.get_text(), "url": item.get("href")} for item in dayhot]

        img = soup.select(".bbc-j1srjl img")
        img = [{"img": item.get("src")} for item in img]

        # monthhot = soup.select("#d-3>li>a")
        # monthhot = [{"word": item.get_text(), "url": item.get("href")} for item in monthhot]

        for i in range(len(dayhot)):
            dayhot[i].update(img[i])

        # print(dayhot)
        return dayhot

    else:
        print("请求失败")

def get_news_detail(item):
    url = item['url']  # 替换为你的URL
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0',

    }
    response = requests.get(url,headers=headers)

    if response:
        html_content = response.text
        return html_content

    else:
        print("请求失败")
