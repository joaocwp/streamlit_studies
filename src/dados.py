import pandas as pd
from streamlit import session_state as session

class Dados:
    def __init__(self):
        self.dados = pd.DataFrame()
        self.resultado = pd.DataFrame()

def init():
    if 'dados' not in session:
        dados = Dados()
        session.dados = dados