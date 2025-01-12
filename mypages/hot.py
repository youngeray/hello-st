import streamlit as st
import pandas as pd
from scripts.weibohot import get_weibo_hot
from scripts.toutiaohot import get_toutiao_hot
from scripts.thepaper import get_thepaper_hot
from scripts.ithome import get_ithome_hot

# st.set_page_config(page_title="新闻热点",page_icon="🔥",layout="wide")

@st.cache_data(ttl=10)
def get_weibo():
    weibo_data = get_weibo_hot()
    return weibo_data

@st.cache_data(ttl=10)
def get_toutiao():
    toutiao_data = get_toutiao_hot()
    return toutiao_data

@st.cache_data(ttl=10)
def get_thepaper():
    thepaper_data = get_thepaper_hot()
    return thepaper_data

@st.cache_data(ttl=10)
def get_ithome():
    ithome_data = get_ithome_hot()
    return ithome_data




weibo,toutiao,thepaper,ithome = st.tabs(["微博热搜",'头条热点','澎湃新闻','IT之家'])


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
            'Url':st.column_config.LinkColumn('详情',display_text='查看',width=50,disabled=True)

        },
        height=500,
    )

def part3():
    thepaper.dataframe(
        get_thepaper(),
        column_config={
            'name':'热点',
            'smallPic':st.column_config.ImageColumn('预览',width=70),
            'url':st.column_config.LinkColumn('详情',display_text='查看',width=50,disabled=True),
            'tagList':st.column_config.ListColumn('标签',width="medium")

        },
        height=500,
    )

def part4():
    ithome.header('今日热点')
    ithome.dataframe(
        get_ithome()['dayhot'],
        column_config={
            'word':st.column_config.TextColumn('热点',width=600,disabled=True),
            'url':st.column_config.LinkColumn('详情',display_text='查看',width=50,disabled=True),
        },
        height=500,
    )

    ithome.header('本周热点')
    ithome.dataframe(
        get_ithome()['weekhot'],
        column_config={
            'word':st.column_config.TextColumn('热点',width=600,disabled=True),
            'url':st.column_config.LinkColumn('详情',display_text='查看',width=50,disabled=True),
        },
        height=500,
    )

    ithome.header('本月热点')
    ithome.dataframe(
        get_ithome()['monthhot'],
        column_config={
            'word':st.column_config.TextColumn('热点',width=600,disabled=True),
            'url':st.column_config.LinkColumn('详情',display_text='查看',width=50,disabled=True),
        },
        height=500,
    )


part1()
part2()
part3()
part4()