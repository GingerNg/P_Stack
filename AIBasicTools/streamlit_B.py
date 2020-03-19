import requests
import pandas as pd
import numpy as np
import streamlit as st
"""
开发展示类型的应用

启动：
streamlit run streamlit_B.py
"""

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)


df = pd.DataFrame({"A": np.linspace(1, 5, 5)})
st.dataframe(df)


# if __name__ == "__main__":
#     st.markdown('# streamDemo')
#     st.markdown('---')
#     sidebar = st.sidebar
#     alo_type = sidebar.selectbox("可视化算法",('pca', 'tsne', 'lle'))
#     data_type = sidebar.selectbox("数据集", ('iris', 'digits'))
#     data, label = load_data(data_type)
#     st.dataframe(data)
#     st.markdown('---')

#     if sidebar.button('run'):
#             df = process(alo_type, data, label)
#     vega_scatter(df)
