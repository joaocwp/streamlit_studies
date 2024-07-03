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
    uploaded_file = st.file_uploader("Choose a file", key='upload_file')
    if st.button('Upload'):
        click()
    
    if session.upload_btn_click:
        df = pd.read_csv(uploaded_file)
        dados.dados = df
        blocks.create_df_block(uploaded_file.name)


def check_column_to_bump(bump_names=None):
    # breakpoint()
    if bump_names is None:
        print('checking bumps...')
        bump_names = [i for i in session['bump_dict']]
        print('keys:', bump_names)
    
    for bump_name in bump_names:
        print('processing:', bump_name)
        bump_dict = session['bump_dict'][bump_name]
        # dataset = bump_dict['dataset']
        col = bump_dict['bump_column']
        val = bump_dict['bump_value']
        status = bump_dict['status']
        order = (bump_dict['order'] == session['order_of_bumping'])
        if not status and order:
            print('to bump:', col)
            print('value:', val)
            dados.dados[col] += val
            session['bump_dict'][bump_name]['status'] = True

    
def compile_bumps(bump_names=None):
    if bump_names is None:
        print('checking bumps...')
        bump_names = [i for i in session['bump_dict']]
        print('keys:', bump_names)
    
    for bump_name in bump_names:
        print('processing:', bump_name)
        bump_dict = session['bump_dict'][bump_name]
        # dataset = bump_dict['dataset']
        col = bump_dict['bump_column']
        val = bump_dict['bump_value']
        status = bump_dict['status']
        mtm = bump_dict['mtm_column']
        mtm_orig = bump_dict['mtm_orig']
        order = (bump_dict['order'] == session['order_of_bumping'])
        if status and order:
            bump_mtm = dados.resultado[mtm]
            dados.resultado[mtm] = mtm_orig
            dados.dados[mtm] = mtm_orig
            dados.dados[col] -= val
            session['bump_dict'][bump_name] = bump_mtm
            dados.resultado[bump_name] = bump_mtm
            print('----------orig:',dados.resultado[mtm].head())
            print('----------bump:',dados.resultado[bump_name].head())
            session['order_of_bumping'] += 1


def clean_bumps():
    print("reseting bumps...")
    if 'bump_dict' in session:
        del session['bump_dict']
    if 'order_of_bumping' in session:
        del session['order_of_bumping']
