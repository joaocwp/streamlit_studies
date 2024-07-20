import streamlit as st
import aba_barfi as aba_barfi
from streamlit import session_state as session

def run():
    tab_barfi, tab_loop, tab_cache = st.tabs(['barfi', 'loop', 'cache'])
    with tab_cache:
        if st.button('Limpar cache'):
            st.cache_data.clear()
            for key in st.session_state.keys():
                del st.session_state[key]
            st.write(st.session_state)
    

    with tab_barfi:
        aba_barfi.run()

if __name__ == '__main__':
    run()
