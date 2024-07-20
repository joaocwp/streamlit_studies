from Barfi import barfi_schemas, st_barfi
import streamlit as st
from streamlit import session_state as session
if 'dados' not in session:
    session.dados = 0
if 'saida' not in session:
    session.saida = None
import blocks
import joblib

print("========================Setup==========================")
blocks.init()
schemas = barfi_schemas()
barfi_schema_name = 'teste4' #st.selectbox('Select a saved schema to load:', schemas)
barfi = st_barfi(compute_engine=True, key='barfi',
                base_blocks=session.blocks,
                load_schema=barfi_schema_name,
                run=True)
if 'saida' in session:
    print(session.saida)