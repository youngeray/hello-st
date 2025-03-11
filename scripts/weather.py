import requests
import streamlit as st
import json


def get_weather():

    myipurl = st.secrets['myip_url']
    response = requests.get(myipurl)
    country = response.json()['network']['location']['country']
    city = response.json()['network']['location']['city']
    district = response.json()['network']['location']['district']
    ip = response.json()['network']['ip']
    location = f'{country}-{city}-{district}'
    print(location,ip)

    weatherurl = st.secrets['weather_url'] + district  # 替换为你的URL
    wresponse = requests.get(weatherurl)

    if wresponse:
        data = wresponse.json()['data']['moji']['data']['forecast']
        # realtime_json = json.dumps(realtime,ensure_ascii=False, indent=4)
        new_data = [{"日期":item["date"],"白天":item["dayWeather"], "夜晚": item["nightWeather"],"最低温度℃":int(item["temperature"].replace('℃','').split('~')[0]),"最高温度℃":int(item["temperature"].replace('℃','').split('~')[1]),"湿度":item["humidity"],"白天风向":item["windDay"],"夜间风向":item["windNight"],"空气质量":item["airQuality"],} for item in data]
        # new_json = json.dumps(new_data, ensure_ascii=False, indent=4)
        # print(data)
        return {'city':location,'data':new_data}

    else:
        print("请求失败")

