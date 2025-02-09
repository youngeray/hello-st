import streamlit as st
import streamlit_shadcn_ui as ui
import pandas as pd
import numpy as np


st.set_page_config(layout="wide")

def index():
    st.title("主页")    
    # st.page_link("app.py",label="主页",icon="🏠")
    st.page_link("mypages/hot.py",label="新闻热点",icon="📈")
    st.page_link("mypages/bbcnews.py",label="BBC中文",icon="📰")
    st.page_link("mypages/zuqiunews.py",label="足球新闻",icon="⚽")
    st.page_link("mypages/weathers.py",label="24天气",icon="🌤️")
    st.page_link("mypages/glmai.py",label="AI绘图",icon="🖼️")


pages = {
    "首页":[st.Page(index,title="首页",icon="🏠")],
    "新闻热点":[st.Page('mypages/hot.py',title="新闻热点",icon="🔥"),st.Page('mypages/bbcnews.py',title="BBC中文",icon="📰"),st.Page('mypages/zuqiunews.py',title="足球新闻",icon="⚽")],
    "24天气":[st.Page('mypages/weathers.py',title="天气查询",icon="🌤️")],
    "智能AI":[st.Page('mypages/glmai.py',title="AI绘图",icon="🖼️")],
    "数据分析":[st.Page('mypages/bi.py',title="BI分析",icon="📊"),st.Page('mypages/example.py',title="例子",icon="🔥")]
}

pg = st.navigation(pages)

pg.run()
