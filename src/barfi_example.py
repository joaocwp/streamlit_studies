from barfi import st_barfi, barfi_schemas
import streamlit as st
from blocks import math_blocks
import dados


def run()
    if 'result' not in st.session_state:
        st.session_state.result = 0

    if 'loop' not in st.session_state:
        st.session_state.loop = False

    if 'n_loops' not in st.session_state:
        st.session_state.n_loops = 0

    if 'counter' not in st.session_state:
        st.session_state.counter = 0

    dados.raw = 0

    st.write(f"Session result: {st.session_state.result}")
    loop = st.button('loop')

    # compute_engine = st.checkbox('Activate barfi compute engine', value=False)
    barfi_schema_name = st.selectbox(
        'Select a saved schema to load:', barfi_schemas())
    barfi_result = st_barfi(
        base_blocks=math_blocks, compute_engine=True, load_schema=barfi_schema_name)

    if not st.session_state.loop:
        st.session_state.n_loops = st.number_input(value=10, label='n_loops')
        st.session_state.loop = loop

    if st.session_state.loop:
        if st.session_state.counter < st.session_state.n_loops:
            st.session_state.result = dados.raw
            st.session_state.counter += 1
        else:
            st.session_state.loop = False
        st.rerun()

