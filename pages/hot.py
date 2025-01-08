import streamlit as st
import pandas as pd
from scripts.weibohot import get_weibo_hot
from scripts.toutiaohot import get_toutiao_hot

st.set_page_config(page_title="新闻热点",page_icon="🔥",layout="wide")

@st.cache_data(ttl=120)
def get_weibo():
    weibo_data = get_weibo_hot()
    return weibo_data

@st.cache_data(ttl=120)
def get_toutiao():
    toutiao_data = get_toutiao_hot()
    return toutiao_data

weibo,toutiao = st.tabs(["微博热搜",'头条热点'])

@st.fragment()
def part1():
    weibo.dataframe(
        get_weibo(),
        column_config={
            "word":"热点",
            "num":"热度"
        },
        height=500,
        width=600
    )

@st.fragment()
def part2():
    toutiao.dataframe(
        get_toutiao(),
        column_config={
            'Title':'热点',
            'HotValue':'热度',
            'LabelUrl':st.column_config.ImageColumn('类型',width=70),
            'Url':st.column_config.LinkColumn('详情',display_text='查看',width=50)

        },
        height=500,
    )

part1()
part2()