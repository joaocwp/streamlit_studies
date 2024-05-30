import pandas as pd
import numpy as np
import streamlit as st
import dados


def upload_file():
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # Can be used wherever a "file-like" object is accepted:
        df = pd.read_csv(uploaded_file)
        st.write(df.head(1))
        dados.dados = df