import streamlit as st
from zhipuai import ZhipuAI

def get_image(prompt):
    key = st.secrets["api_key"]
    client = ZhipuAI(api_key=key) # 请填写您自己的APIKey
    
    response = client.images.generations(
        model="cogview-3-flash", #填写需要调用的模型编码
        prompt=prompt,
    )

    print(response.data[0].url)
    return response.data[0].url
