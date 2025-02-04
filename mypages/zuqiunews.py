import streamlit as st
import pandas as pd
from scripts.zuqiu import get_zuqiu_hot

# st.set_page_config(page_title="新闻热点",page_icon="🔥",layout="wide")

@st.cache_data(ttl=60)
def get_zuqiu():
    zuqiu_data = get_zuqiu_hot()
    return zuqiu_data[140:]

get_zuqiu()

for item in get_zuqiu():
    st.markdown(f'- [{item["word"]}]({item["url"]})')

