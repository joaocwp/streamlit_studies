import streamlit as st
import aba_barfi as aba_barfi
import aba_loop as aba_loop

def run():
    aba_barfi.init()
    tab_barfi, tab_loop = st.tabs(['barfi','loop'])

    with tab_barfi:
        aba_barfi.run()

    with tab_loop:
        st.write("Under development")

if __name__ == '__main__':
    run()
