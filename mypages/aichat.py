import streamlit as st
from zhipuai import ZhipuAI

key = st.secrets["api_key"]
client = ZhipuAI(api_key=key) # 请填写您自己的APIKey

# 设置页面标题
st.title("AI 聊天助手")

# 初始化会话历史
if "messages" not in st.session_state:
    st.session_state.messages = []

# 显示历史消息
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 用户输入
if prompt := st.chat_input("请输入您的问题"):
    # 添加用户消息到历史
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # 显示用户消息
    with st.chat_message("user"):
        st.markdown(prompt)

    # 显示助手消息框
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # 创建流式响应
        response = client.chat.completions.create(
            model="glm-4-flash",  # 或其他支持的模型
            messages=[{"role": m["role"], "content": m["content"]} 
                     for m in st.session_state.messages],
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
    st.session_state.messages.append({"role": "assistant", "content": full_response})

