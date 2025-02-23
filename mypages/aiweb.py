import streamlit as st
from zhipuai import ZhipuAI
from scripts.webcontent import get_web

key = st.secrets["api_key"]
client = ZhipuAI(api_key=key) # 请填写您自己的APIKey


# 初始化会话历史
if "messages" not in st.session_state:
    st.session_state.messages = []

# 显示历史消息
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# 用户输入

if webcontent := st.chat_input("请输入网址"):
    prompt = get_web(webcontent)

    # 添加用户消息到历史
    # st.session_state.messages.append({"role": "user", "content": prompt})
    
    # 显示用户消息
    with st.chat_message("user"):
        st.markdown(webcontent)

    # 显示助手消息框
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # 创建流式响应
        response = client.chat.completions.create(
            model="glm-4-flash",  # 或其他支持的模型
            messages=[
                {"role": "system", "content": "你是一个ai新闻助手，根据用户输入的新闻网页中的内容，整理出新闻标题和对应的链接"},
                {"role": "user", "content": f'请整理出以下网页中的新闻，以markdown的格式输出新闻标题和对应的链接：{prompt}'},
            ],
            stream=True
        )
        
        # 逐步显示响应内容
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                full_response += chunk.choices[0].delta.content
                message_placeholder.markdown(full_response + "▌")
        
        # 显示完整响应
        message_placeholder.markdown(full_response)
    
    # 将助手回复添加到历史
    # st.session_state.messages.append({"role": "assistant", "content": full_response})

