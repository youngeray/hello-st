import streamlit as st
import streamlit_shadcn_ui as ui
import pandas as pd
import numpy as np


st.set_page_config(page_title="示例",page_icon="🔥")

options = st.multiselect(
    "What are your favorite colors",
    ["Green", "Yellow", "Red", "Blue"],
    ["Yellow", "Red"],
)

st.write("You selected:", options)

cols = st.columns(3)
with cols[0]:
    ui.metric_card(title="Total Revenue", content="$45,231.89", description="+20.1% from last month", key="card1")
with cols[1]:
    ui.metric_card(title="Total Revenue", content="$45,231.89", description="+20.1% from last month", key="card2")
with cols[2]:
    ui.metric_card(title="Total Revenue", content="$45,231.89", description="+20.1% from last month", key="card3")

clicked = ui.button("Click", key="clk_btn",variant="outline")
st.write("UI Button Clicked:", clicked)

st.button("Click",type="primary")
st.button("Click",type="secondary",icon="🔥")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["河北", "山东", "河南"])

st.line_chart(chart_data,x_label="时间",y_label="温度")


uploaded_img = st.file_uploader("Choose a img")
if uploaded_img is not None:
    # To read file as bytes:
    bytes_data = uploaded_img.getvalue()
    st.image(bytes_data)

uploaded_vd = st.file_uploader("Choose a video")
if uploaded_vd is not None:
    # To read file as bytes:
    bytes_data = uploaded_vd.getvalue()
    st.video(bytes_data,format="video/mp4")


uploaded_ad = st.file_uploader("Choose a audio")
if uploaded_ad is not None:
    # To read file as bytes:
    bytes_data = uploaded_ad.getvalue()
    st.audio(bytes_data,format="audio/mpeg")






