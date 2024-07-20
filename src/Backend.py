from Barfi import ComputeEngine
from streamlit import session_state as session

def get_execution(fluxo):
    _ce = ComputeEngine(blocks=session.blocks)
    _ce.add_editor_state(fluxo)
    _ce._map_block_link()
    _ce._execute_compute()