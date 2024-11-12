from Barfi import barfi_schemas, st_barfi
# from Barfi.StBarfi import StBarfi
import streamlit as st
from streamlit import session_state as session
import utils
import blocks
import joblib
import CustomBlockBuilder
from copy import deepcopy
import pathlib
from datetime import datetime
import time


if 'blocks' in session:
    del session.blocks


print("========================Setup==========================")
utils.init()
utils.upload_file()
utils.upload_code()
blocks.init()
utils.import_blocks()
schemas = barfi_schemas()
# custom_block_schemas = st.multiselect("select schemas for custom block building", schemas)
# custom_block_schemas = ['entradas', 'custom']
# file = joblib.load('schemas.barfi')
# fluxos = {i:file[i] for i in file if i in custom_block_schemas}
# CustomBlockBuilder.init(fluxos)
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
    file = joblib.load('schemas.barfi')
    fluxo = file[barfi_schema_name]
    config = {'session': aux, 'fluxo': fluxo}
    timestamp = datetime.now().strftime('%s')
    session['wkp'] = 'wkp'
    session['ts'] = timestamp
    joblib.dump(config, f'{session["wkp"]}_{timestamp}.configjson')

if st.button('Get results'):
    processed = False
    c = 0
    with st.spinner(f"Waiting for results..."):
        while not processed and c < 30:
            try:
                print("Lendo:", f"{session['wkp']}_{session['ts']}.result.json")
                result_dict = joblib.load(f"{session['wkp']}_{session['ts']}.result.json")
                st.write(f"Resultado: {result_dict['saida']}")
                print("Limpando resultado...")
                tmp_rem = pathlib.Path(f"{session['wkp']}_{session['ts']}.result.json")
                tmp_rem.unlink()
                processed = True
            except Exception as e:
                print(e)
                c += 1
                print('Aguardando:', c)
                time.sleep(1)