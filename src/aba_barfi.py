from Barfi import st_barfi, barfi_schemas, Block
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
        print("Setup")
        # print(blocks.blocks)
        # bump_keys = [i for i in session if 'bump_' in i]
        st_barfi(base_blocks=blocks.blocks, compute_engine=True,
                  load_schema=barfi_schema_name, key=f'barfi', run=run)
    utils.clean_bumps()
    st.write(dados.resultado)

