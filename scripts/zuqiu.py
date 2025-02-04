import requests
from bs4 import BeautifulSoup
import json
import streamlit as st

def get_zuqiu_hot():
    url = st.secrets['zuqiu_url']  # 替换为你的URL
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0',

    }
    response = requests.get(url,headers=headers)

    if response:
        response.encoding = 'utf-8'
        html_content = response.text
        soup = BeautifulSoup(html_content, 'lxml')

        dayhot = soup.select("div.content ul li a")
        dayhot = [{"word": item.get_text(), "url": item.get("href")} for item in dayhot]


        print(dayhot)
        return dayhot

    else:
        print("请求失败")
