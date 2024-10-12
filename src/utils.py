import pandas as pd
import streamlit as st
from streamlit import session_state as session
import os
from glob import glob
from importlib import reload
import tempDir as tmp

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

def upload_code():
    uploaded_code = st.file_uploader("Choose a code", key='upload_code')
    if uploaded_code is not None:
        with open(os.path.join("tempDir", uploaded_code.name),"wb") as f:
            f.write(uploaded_code.getbuffer())

def import_blocks():
    files = glob('tempDir/*.py')
    pynames = [i.replace('tempDir/','').replace('.py', '') for i in files if '__init__' not in i]
    for file in pynames:
        try:
            print("Buscando blocos")
            reload(tmp)
            block = eval(f'tmp.{file}.init()')
            session.blocks.append(block)
        except Exception as e:
            print('erro:',e)
