from Barfi import barfi_schemas, st_barfi
# from Barfi.StBarfi import StBarfi
import streamlit as st
from streamlit import session_state as session
import utils
import blocks
import joblib
import CustomBlockBuilder
from copy import deepcopy

if 'blocks' in session:
    del session.blocks


print("========================Setup==========================")
utils.init()
utils.upload_file()
blocks.init()
schemas = barfi_schemas()
custom_block_schemas = st.multiselect("select schemas for custom block building", schemas)
custom_block_schemas = ['entradas', 'custom']
file = joblib.load('schemas.barfi')
fluxos = {i:file[i] for i in file if i in custom_block_schemas}
CustomBlockBuilder.init(fluxos)
barfi_schema_name = st.selectbox('Select a saved schema to load:', schemas)
# if barfi_schema_name is None:
#     barfi_schema_name = 'teste'
run = False #st.button('run')
st_barfi(compute_engine=True, key='barfi',
                base_blocks=session.blocks,
                load_schema=barfi_schema_name)
if 'saida' in session:
    st.write(session.saida)

if st.button("Save session"):
    aux = deepcopy(dict(session))
    del aux['blocks']
    joblib.dump(aux, 'session_state.pkl')
