import streamlit as st
import pandas as pd
from scripts.weather import get_weather

# st.set_page_config(page_title="新闻热点",page_icon="🔥",layout="wide")

@st.cache_data(ttl=10)
def get_weathers():
    weather_data = get_weather()
    return weather_data




weathers, = st.tabs(["24小时",])


@st.fragment()
def part1():
    weathers.dataframe(
        get_weathers(),
        height=200,
        width=600
    )

    weather_data = pd.DataFrame(get_weathers())
    weathers.line_chart(weather_data,x="时间",y="温度")

part1()