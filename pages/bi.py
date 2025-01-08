import streamlit as st
import pandas as pd
from pygwalker.api.streamlit import StreamlitRenderer

st.set_page_config(page_title="数据分析",page_icon="🔥",layout="wide")

st.header("数据分析")
df = pd.read_csv("https://kanaries-app.s3.ap-northeast-1.amazonaws.com/public-datasets/bike_sharing_dc.csv")
pyg_app = StreamlitRenderer(df)
pyg_app.explorer()

