import streamlit as st
from streamlit import session_state as session
import dados


result_ctn = st.expander(label='Resultado', expanded=True)

def render():
    with result_ctn:
        st.write(dados.dados)