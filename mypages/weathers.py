import streamlit as st
import pandas as pd
from scripts.weather import get_weather

# st.set_page_config(page_title="新闻热点",page_icon="🔥",layout="wide")

@st.cache_data(ttl=100)
def get_weathers():
    weather_data = get_weather()
    return weather_data




weathers, = st.tabs(["24小时",])


@st.fragment()
def part1():

    data = get_weathers()["data"]
    location = get_weathers()["city"]
    weather_data = pd.DataFrame(data)


    with weathers.container():
        weathers.markdown(f'#### {location} 天气预报')
        weathers.dataframe(
            data,
            height=200,
            width=600
        )


        
    with weathers.container():
        weathers.markdown("---")
        weathers.line_chart(weather_data,x="日期",y=["最高温度℃","最低温度℃"])

part1()