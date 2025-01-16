import streamlit as st
from scripts.cogview import get_image


prompt = st.chat_input("请输入图像描述")
if 'all_images' not in st.session_state:
    st.session_state.all_images = []
if prompt:
    image_url = get_image(prompt)
    image_data = {
        "url": image_url,
        "prompt": prompt
    }
    st.session_state.all_images.append(image_data)
    for image in st.session_state.all_images:
        st.image(image['url'],caption=image['prompt'],width=300)
        


