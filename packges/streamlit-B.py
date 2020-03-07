import streamlit as st

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)

import numpy as np
import pandas as pd

df = pd.DataFrame({"A": np.linspace(1, 5, 5)})
st.dataframe(df)