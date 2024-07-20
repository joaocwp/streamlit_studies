import pandas as pd
import streamlit as st
from streamlit import session_state as session

print('import utils')
def init():
    print('init dados')
    if 'dados' not in session:
        session.dados = pd.DataFrame()

def click():
    session.upload_btn_click = True

def upload_file():
    if 'upload_btn_click' not in session:
        session.upload_btn_click = False

    uploaded_file = st.file_uploader("Choose a file", key='upload_file')
    if st.button('Upload'):
        print('uploading')
        df = pd.read_csv(uploaded_file)
        session.dados = df.copy()
