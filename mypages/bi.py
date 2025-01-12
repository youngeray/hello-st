import streamlit as st
import pandas as pd
from pygwalker.api.streamlit import StreamlitRenderer


st.header("数据分析")

uploaded_file = st.file_uploader('选择文件',type=['csv','xlsx','xls'])
if uploaded_file is not None:
    try:
        # 根据文件类型选择不同的读取方法
        file_extension = uploaded_file.name.split('.')[-1].lower()
        
        if file_extension == 'csv':
            try:
                df = pd.read_csv(uploaded_file)
            except UnicodeDecodeError:
                df = pd.read_csv(uploaded_file, encoding='gbk')
        else:  # Excel文件
            df = pd.read_excel(uploaded_file)
            
        if df.empty:
            st.error('文件是空的，请上传包含数据的文件。')
        else:
            st.success('文件加载成功！')
            # 显示数据基本信息
            st.write(f"数据行数: {df.shape[0]}, 列数: {df.shape[1]}")
            pyg_app = StreamlitRenderer(df)
            pyg_app.explorer()
            
    except pd.errors.EmptyDataError:
        st.error('文件是空的，请上传包含数据的文件。')
    except Exception as e:
        st.error(f'读取文件时发生错误: {str(e)}')

