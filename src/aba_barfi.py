from Barfi.StBarfi import StBarfi, barfi_schemas
# from Barfi import Block
import streamlit as st
from streamlit import session_state as session
import utils
import blocks
import dados


def run():
    barfi_schema_name = st.selectbox(
        'Select a saved schema to load:', barfi_schemas())
    run = False #st.button('run')
    barfi_ctn = st.expander(label='Barfi',  expanded=True)

    with barfi_ctn:
        print("========================Setup==========================")
        bump_keys = ['init'] + [i for i in session if 'bump_' in i]
        i = 0
        barfi = StBarfi(base_blocks=blocks.blocks, compute_engine=True,
                    load_schema=barfi_schema_name, key='barfi')
        while i < len(bump_keys):
            barfi.run_barfi(run=True)
            bump_keys = ['init'] + [i for i in session if 'bump_' in i]
            print(f'{i} --------------- {bump_keys[i]}')
            i += 1

    utils.clean_bumps()
    st.write(dados.resultado)

