from Barfi import ComputeEngine
from streamlit import session_state as session
import blocks
import joblib
import utils
from copy import deepcopy
import time
import pathlib


#Se executando em backend real, precisamos re-inicializar os blocos

def get_execution(fluxo, blocos):
    _ce = ComputeEngine(blocks=blocos)
    _ce.add_editor_state(fluxo)
    _ce._map_block_link()
    _ce._execute_compute()

def init_session(session_dict):
    for key in session_dict:
        session[key] = deepcopy(session_dict[key])

def save_results(session_dict):
    aux = deepcopy(session_dict)
    del aux['blocks']
    joblib.dump(aux, 'resultado.json')

while True:
    config = None
    try:
        config = joblib.load('config.json')
    except:
        time.sleep(1)
    
    if config is not None:
        fluxo = config['fluxo']
        init_session(config['session'])
        # session = deepcopy(config['session'])
        print("========================Setup==========================")
        blocks.init()
        utils.import_blocks()
        get_execution(fluxo, session['blocks'])
        print(f'fluxo executado. Salvando resultados...')
        save_results(session)
        print('limpando config...')
        tmp_rem = pathlib.Path('config.json')
        tmp_rem.unlink()
        print(f'config.json deletado')
