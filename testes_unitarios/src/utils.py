import streamlit as st
import pandas as pd
import numpy as np
import math_util
import beholder


from streamlit import session_state as session

def get_max_order():
    if 'config' in session:
        return max([session['config'][i]['order'] for i in session['config']])
    return 0

def fix_max_order():
    if 'config' in session:
        for i in session['config']:
            session['config'][i]['order'] = 1
    return 0

@st.cache_data()
def get_addition(a=1, b=2):
    return math_util.add(a, b)

def get_subtraction():
    return math_util.subtract(1, 2)

@st.cache_data()
def get_multiplication():
    return math_util.multiply(1, 2)
