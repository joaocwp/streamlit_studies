import pandas as pd
import numpy as np
import streamlit as st
import dados

# def get_df():
#     df = pd.DataFrame({'id':np.tile(np.arange(10), 10)})
#     df['value'] = np.arange(len(df))
#     return df


def run_cumsum(dataframe):
    aux = dataframe.copy()
    aux['cs'] = aux.value.cumsum()
    return aux


def add_click():
    st.session_state.click_number += 1
    # if st.session_state.click_number > len(st.session_state.unique_ids):
    #     st.write("Fim de jogo")
    #     st.session_state.looping = False
    if st.session_state.click_number > 0:
        st.session_state.unique_ids = list(dados.df.id.unique())
        id = st.session_state.unique_ids[st.session_state.click_number-1]
        st.write(f"id: {id}")
        tmp = dados.df.loc[dados.df.id==id]
        st.session_state.result = pd.concat([st.session_state.result, run_cumsum(tmp)])
