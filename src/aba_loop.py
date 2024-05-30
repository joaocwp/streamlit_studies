import streamlit as st
import pandas as pd
import numpy as np
import utils
import dados

def run():
    # Session State also supports attribute based syntax
    if 'click_number' not in st.session_state:
        st.session_state.click_number = 0

    if 'result' not in st.session_state:
        st.session_state.result = pd.DataFrame()

    if 'unique_ids' not in st.session_state:
        st.session_state.unique_ids = []
    
    if 'looping' not in st.session_state:
        st.session_state.looping = False
    
    if 'click' not in st.session_state:
        st.session_state.click = False

    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # Can be used wherever a "file-like" object is accepted:
        df = pd.read_csv(uploaded_file)
        st.write(df.head(1))
        dados.df = df

    st.write(f"loop: ", st.session_state.looping)
    st.write(f"Número de clicadas: {st.session_state.click_number}")

    click = st.button("Clicae")

    if st.session_state.click_number > 0:
        st.dataframe(st.session_state.result)

    if not st.session_state.looping:
        st.session_state.looping = st.button("loop")

    if (st.session_state.looping) | click:
        utils.add_click()
        if st.session_state.click_number >= len(st.session_state.unique_ids):
            st.write("Fim de jogo")
            st.session_state.looping = False
        st.rerun()


if __name__ == '__main__':
    run()
