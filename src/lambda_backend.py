from Barfi import ComputeEngine
from streamlit import session_state as session
import blocks
import joblib
import utils
from copy import deepcopy
import time
import pathlib
from glob import glob


#Se executando em backend real, precisamos re-inicializar os blocos

def get_execution(fluxo, blocos):
    _ce = ComputeEngine(blocks=blocos)
    _ce.add_editor_state(fluxo)
    _ce._map_block_link()
    _ce._execute_compute()

def init_session(session_dict):
    for key in session_dict:
        session[key] = deepcopy(session_dict[key])

def save_results(session_dict, resname):
    aux = deepcopy(session_dict)
    del aux['blocks']
    joblib.dump(aux.to_dict(), f'{resname}.result.json')

while True:
    config = None
    print("buscando config...")
    files = glob('*.configjson')
    if len(files) > 0:
        try:
            filename = files[0]
            print("Lendo config...")
            config = joblib.load(filename)
        except:
            pass
    else:
        time.sleep(10)
    
    if config is not None:
        print('limpando config...')
        tmp_rem = pathlib.Path(files[0])
        tmp_rem.unlink()
        print(f'configjson deletado')
        fluxo = config['fluxo']
        init_session(config['session'])
        # session = deepcopy(config['session'])
        print("========================Setup==========================")
        blocks.init()
        utils.import_blocks()
        get_execution(fluxo, session['blocks'])
        print(f'fluxo executado. Salvando resultados...')
        resname = files[0].split('.')[0]
        save_results(session, resname)
