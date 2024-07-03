from Barfi.StBarfi import StBarfi, barfi_schemas
# from Barfi import Block
import streamlit as st
from streamlit import session_state as session
import utils
import blocks
import dados
import joblib


def run():
    barfi_schema_name = st.selectbox(
        'Select a saved schema to load:', barfi_schemas())
    run = False #st.button('run')
    barfi_ctn = st.expander(label='Barfi',  expanded=True)

    with barfi_ctn:
        print("========================Setup==========================")
        barfi = StBarfi(base_blocks=blocks.blocks, compute_engine=True,
                    load_schema=barfi_schema_name, key='barfi')
    if st.button('Save pkl', key='save_btn'):
        joblib.dump(barfi, 'barfi.pkl')
    utils.clean_bumps()

    st.write(dados.resultado)

    # if st.button('load pkl', key='load_btn'):
    #     breakpoint()
    #     barfi = joblib.load('barfi.pkl')
    #     print('dados:',dados.resultado.head(2))
    #     barfi.run_barfi(run=True)
    #     print('dados pos run:',dados.resultado.head(2))
    #     utils.clean_bumps()
    #     st.write(dados.resultado)

