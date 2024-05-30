from barfi import st_barfi, barfi_schemas, Block
import streamlit as st
from streamlit import session_state as session
import utils
import blocks
import dados


def init():
    if 'id' not in session:
        session.id = 0
    if 'result' not in session:
        print("inicializando")
        session.result = 0
    if 'loop' not in session:
        session.loop = False
    if 'n_loops' not in session:
        session.n_loops = 0
    if 'counter' not in session:
        session.counter = 0

def run():
    utils.upload_file()
    st.write(f"Result: {session.result}")
    st.write(f"loops: {session.counter}, id: {session.id}")

    loop = st.button('loop')

    barfi_schema_name = st.selectbox(
        'Select a saved schema to load:', barfi_schemas())
    st_barfi(base_blocks=blocks.math_blocks, compute_engine=True, load_schema=barfi_schema_name)

    if not session.loop:
        session.n_loops = st.number_input(value=9, label='n_loops')
        session.loop = loop

    if session.loop:
        if session.counter < session.n_loops:
            session.result += dados.raw
            session.counter += 1
            session.id = session.counter
        else:
            session.loop = False
        st.rerun()
    st.write(f"run: {dados.raw}")

