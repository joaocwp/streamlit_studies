import pandas as pd
import numpy as np
import streamlit as st
import dados
import blocks
from streamlit import session_state as session

def click():
    session.upload_btn_click = True

def upload_file():
    if 'upload_btn_click' not in session:
        session.upload_btn_click = False
    uploaded_file = st.file_uploader("Choose a file")
    if st.button('Upload'):
        click()
    
    if session.upload_btn_click:
        df = pd.read_csv(uploaded_file)
        dados.dados = df
        blocks.create_df_block(uploaded_file.name)

def check_for_bumps(bump_keys=None):
    if bump_keys is None:
        print('checking bumps...')
        bump_keys = [i for i in session if 'bump_' in i]
        print('keys:', bump_keys)

    for key in bump_keys:
        print('processing:', key)
        # breakpoint()
        bump_dict = session[key]
        # dataset = bump_dict['dataset']
        col = bump_dict['bump_column']
        val = bump_dict['bump_value']
        status = bump_dict['status']
        mtm = bump_dict['mtm_column']
        mtm_orig = bump_dict['mtm_orig']
        bump_name = bump_dict['bump_name']
        print('status:', status)
        if status:
            # breakpoint()
            bump_mtm = dados.resultado[mtm]
            dados.resultado[mtm] = mtm_orig
            session[bump_name] = bump_mtm
            dados.resultado[bump_name] = bump_mtm
            print('----------orig:',dados.resultado[mtm].head())
            print('----------bump:',dados.resultado[bump_name].head())
        elif not status:
            print('to bump:', col)
            print('value:', val)
            # breakpoint()
            dados.dados[col] += val
            session[key]['status'] = True


def clean_bumps():
    print("reseting bumps...")
    bump_keys = [i for i in session if 'bump_' in i]
    for key in bump_keys:
        print('reseting', key)
        del session[key]