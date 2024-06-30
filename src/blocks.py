from barfi import Block
import streamlit as st
from streamlit import session_state as session
import dados
import utils

global blocks
blocks = []

def init():
    global blocks
    blocks = []
    result_block()
    sum_block()
    bump_block()


def create_df_block(dataframe, name='input'):
    block = Block(name=name.replace('.','_'))
    print('============creating:', block._name)
    for col in dataframe:
        block.add_output(name=col, value={'dataset': dataframe, 'column':col, 'value':dataframe[col]})
    block.add_compute(df_block_func)
    global blocks
    blocks.append(block)

def df_block_func(self):
    # print('pre bump:', dados.dados.head(1))
    utils.check_for_bumps()
    for col in dados.dados:
        self.set_interface(name=col, value={'dataset':dados.dados, 'column':col, 'value':dados.dados[col]})
    # print('pos bump:', dados.dados.head(1))


def result_block_func(self):
    dataset = self.get_interface(name='result')['dataset']
    dados.resultado = dataset

def result_block():
    block = Block(name='result')
    block.add_input(name='result')
    block.add_compute(result_block_func)
    global blocks
    blocks.append(block)


def sum_func(self):
    nome_saida = self._name
    dataset = self.get_interface(name='col1')['dataset']
    col1 = self.get_interface(name='col1')['column']
    col2 = self.get_interface(name='col2')['column']
    dataset[nome_saida] = dataset[col1] + dataset[col2]
    self.set_interface(name='result', value={'dataset': dataset,
                                            'column':nome_saida,
                                            'value':dataset[nome_saida]})

def sum_block():
    sum_block = Block(name='Soma')
    sum_block.add_input(name='col1')
    sum_block.add_input(name='col2')
    sum_block.add_output(name='result')
    sum_block.add_compute(sum_func)
    global blocks
    blocks.append(sum_block)

def bump_block():
    block = Block(name='Bump')
    block.add_input(name='bump col')
    block.add_input(name='mtm col')
    block.add_option(name='valor', type='number', value=0.1)
    block.add_compute(bump_block_func)
    global blocks
    blocks.append(block)

def bump_block_func(self):
    nome_saida = self._name
    bump_col = self.get_interface(name='bump col')['column']
    mtm_col = self.get_interface(name='mtm col')['column']
    dataset = self.get_interface(name='bump col')['dataset']
    value = self.get_option(name='valor')
    value = float(value)

    bump_key = f'bump_{nome_saida}'
    
    if bump_key not in session:
        print('=======cache para bump:', bump_col)
        session[bump_key] = {'dataset':dataset,
                                         'bump_column':bump_col,
                                         'bump_value':value,
                                         'mtm_column':mtm_col,
                                         'mtm_orig':dataset[mtm_col],
                                         'status': False,
                                         'bump_name': nome_saida,
                                         'mtm_bumped':mtm_col}
        st.rerun()
    print('===========compile bump result')
    utils.check_for_bumps(bump_keys=[bump_key])
    # dados.resultado[f'bump_{mtm_col}'] = session[bump_key]['mtm_bumped']
    