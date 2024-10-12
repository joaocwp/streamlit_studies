import streamlit as st
from streamlit import session_state as session
import duckdb as ddb
import pandas as pd
import numpy as np
from datetime import datetime


def run():
    if 'cadastro' not in session:
        session.cadastro = pd.DataFrame({'nome_produto':[None],
                                'tipo':None,
                                'contraparte':None,
                                'quantidade':None,
                                'valor':None
                                })
    try:
        session.base = pd.read_parquet('cadastro_produto.parquet')
    except:
        session.base = pd.DataFrame()

    with st.container():
        with st.form(key='form_busca_produto'):
            nome_produto = st.text_input('Nome do produto')
            try:
                tmp = session.base.loc[session.base.nome_produto == nome_produto]
                tmp = tmp.sort_values('timestamp', ascending=False)
                if len(tmp) > 0:
                    timestamp = st.selectbox('versões', tmp.timestamp)
                    tmp = tmp.loc[tmp.timestamp == timestamp]
                tmp = tmp.drop_duplicates(subset=['nome_produto'], keep='first')
                if len(tmp) == 0:
                    tmp = session.cadastro
            except:
                st.write('Nada encontrado')
                
            if st.form_submit_button('Submit'):
                session.cadastro = tmp.copy()
                del tmp
            

        with st.form(key='form_cadastro_produto'):
            cadastro_editor = session.cadastro.T.copy()
            cadastro_editor = cadastro_editor.astype(str)
            # cadastro_editor.index.name = 'chave'
            # cadastro_editor = cadastro_editor.rename(columns={'0':'valor'})
            cadastro_editor = st.data_editor(cadastro_editor, width=500, num_rows='dynamic')
            session.cadastro = cadastro_editor.T.copy()
            submit = st.form_submit_button('Submit')
            if submit:
                session.cadastro['timestamp'] = datetime.now()
                if session.cadastro.nome_produto[0] is None:
                    st.write("Adicionar o nome do produto")
                else:
                    st.write('Cadastro salvo')
                    session.base = pd.concat([session.base, session.cadastro])
                    session.base.to_parquet('cadastro_produto.parquet')


if __name__ == '__main__':
    run()
