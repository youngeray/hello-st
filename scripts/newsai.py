import streamlit as st
from zhipuai import ZhipuAI

def get_message(prompt):
    key = st.secrets["api_key"]
    client = ZhipuAI(api_key=key) # 请填写您自己的APIKey
    
    response = client.chat.completions.create(
        model="glm-4-flash", #填写需要调用的模型编码
        messages=[
            {"role": "system", "content": "你是一个乐于解答各种问题的助手，你的任务是为用户提供专业、准确、有见地的建议。"},
            {"role": "user", "content": prompt},
        ],
        stream=True,
    )

    # for chunk in response:
    #     print(chunk.choices[0].delta.content)
    print(response)

get_message("请介绍python streamlit库")