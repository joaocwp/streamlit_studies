import streamlit as st
from Barfi.StBarfi import StBarfi
import joblib
import dados
import utils


def run():
    if st.button('load pkl', key='load_btn'):
        barfi = joblib.load('barfi.pkl')
        print('dados:', dados.resultado.head(2))
        barfi.run_barfi(run=True)
        print('dados pos run:', dados.resultado.head(2))
        utils.clean_bumps()
        st.write(dados.resultado)