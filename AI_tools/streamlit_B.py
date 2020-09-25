
# 开发展示类型的应用

# 启动：
# streamlit run streamlit_B.py
# streamlit run streamlit_B.py --server.port 8101 --server.address "192.168.79.137"
# 中文文档
# http://cw.hubwiz.com/card/c/streamlit-manual/


from PIL import Image
import requests
import pandas as pd
import numpy as np
import streamlit as st


def func(text):
    return "ok" + text


def download_url(url):
    if url != "":
        res = requests.get(url)
        open("./data/res.pdf", "wb").write(res.content)
    return "ok"


# 当行文本 传入文件url下载后处理
url = st.text_input('URL', '')
st.write('The current movie title is', download_url(url))


# 图像
image = Image.open('./data/ProgrammingIsAnArtForm.jpg')
st.image(image, caption='Sunrise by the mountains', use_column_width=True)


# 多行文本
txt = st.text_area('Text to analyze', '''
...     It was the best of times, it was the worst of times, it was
...     the age of wisdom, it was the age of foolishness, it was
...     the epoch of belief, it was the epoch of incredulity, it
...     was the season of Light, it was the season of Darkness, it
...     was the spring of hope, it was the winter of despair, (...)
...     ''')
st.write('Sentiment:', func(txt))

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)


x = st.slider('Select a value')
st.write(x, 'squared is', x * x)


# 显示可交互数据帧
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
