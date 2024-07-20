from Barfi import barfi_schemas, st_barfi
# from Barfi.StBarfi import StBarfi
import streamlit as st
from streamlit import session_state as session
import utils
import blocks


def run():
    print("========================Setup==========================")
    utils.init()
    utils.upload_file()
    blocks.init()
    schemas = barfi_schemas()
    barfi_schema_name = st.selectbox('Select a saved schema to load:', schemas)
    # if barfi_schema_name is None:
    #     barfi_schema_name = 'teste'
    run = False #st.button('run')
    barfi = st_barfi(compute_engine=True, key='barfi',
                    base_blocks=session.blocks,
                    load_schema=barfi_schema_name)
    if 'saida' in session:
        st.write(session.saida)


