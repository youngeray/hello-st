import requests
import streamlit as st
import json

def get_weather():
    url = st.secrets['weather_url']  # 替换为你的URL
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'Cookie': 'HWWAFSESTIME=1737033279545; HWWAFSESID=2dc4979020cf649518; moji_setting=%7B%22internal_id%22%3A480%7D; liveview_page_cursor=eyJtaW5JZCI6ODE3NDkxNTQsIm1heElkIjo4MTczNjgyOCwibWluQ3JlYXRlVGltZSI6MTUwNzQyMTY2OTAwMCwibWF4Q3JlYXRlVGltZSI6MTUwNzE3Mzk3NDAwMH0%3D; PHPSESSID=qqjn057dqal029kfht5fae3si2',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0',

    }
    response = requests.get(url,headers=headers)

    if response:
        data = response.json()['hour24']
        # realtime_json = json.dumps(realtime,ensure_ascii=False, indent=4)
        new_data = [{"日期":item["Fpredict_date"],"时间":f'{item["Fpredict_hour"]}:00', "温度": item["Ftemp"],"天气":item["Fcondition"]} for item in data]
        # new_json = json.dumps(new_data, ensure_ascii=False, indent=4)
        # print(data)
        return new_data

    else:
        print("请求失败")

