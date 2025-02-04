import streamlit as st
import pandas as pd
from scripts.bbczw import get_bbczw_hot
from scripts.bbczw import get_news_detail

# st.set_page_config(page_title="新闻热点",page_icon="🔥",layout="wide")

@st.cache_data(ttl=60)
def get_bbczw():
    bbczw_data = get_bbczw_hot()
    return bbczw_data

@st.dialog("详情",width="large")
def show_news_detail(item):
    news_detail = get_news_detail(item)
    st.html(news_detail)

news = get_bbczw()

for item in news:
    container = st.container(border=True)
    container.markdown(f"##### {item['word']}")
    container.image(item['img'])
    container.button("查看详情",on_click=show_news_detail,args=(item,),key=item['word'])
