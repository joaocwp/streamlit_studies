from barfi import Block
import streamlit as st
from streamlit import session_state as session
# import utils

dados = session.dados
print("import blocks")


def init():

    print('starting blocks')
    session.blocks = []
    constant_block()
    saida_block()
    # create_df_block()
    # result_block()
    # sum_block()
    # bump_block()

def constant_block():
    block = Block(name='constante')
    block.add_option(name='valor', type='integer', value=1)
    block.add_output(name='saida')
    block.add_compute(constant_func)
    session.blocks.append(block)


def constant_func(self):
    nome = self._name
    valor = self.get_option(name='valor')
    session.constante = valor
    self.set_interface(name='saida', value=valor)

def saida_block():
    block = Block(name='saida')
    block.add_input(name='saida')
    block.add_compute(saida_func)
    session.blocks.append(block)

def saida_func(self):
    valor = self.get_interface(name='saida')
    session.saida = valor


# def create_df_block(name='Input'):
#     block = Block(name=name.replace('.','_'))
#     dataframe = dados.dados
#     print('colums:', dataframe.columns)
#     for col in dataframe:
#         print(col)
#         block.add_output(name=col, value={'dataset': dataframe, 'column':col, 'value':dataframe[col]})
#     block.add_compute(df_block_func)
#     global blocks
#     session.blocks.append(block)


# def df_block_func(self):
#     # breakpoint()
#     cols = [i for i in self._outputs]
#     for col in cols:#dados.dados:
#         try:
#             self.set_interface(name=col, value={'dataset':dados.dados, 'column':col, 'value':dados.dados[col]})
#         except:
#             print('Could not set interface for ', col)


# def result_block_func(self):
#     dataset = self.get_interface(name='result')['dataset']
#     dados.resultado = dataset


# def result_block():
#     block = Block(name='result')
#     block.add_input(name='result')
#     block.add_compute(result_block_func)
#     session.blocks.append(block)


# def sum_func(self):
#     nome_saida = self._name
#     dataset = self.get_interface(name='col1')['dataset']
#     col1 = self.get_interface(name='col1')['column']
#     col2 = self.get_interface(name='col2')['column']
#     dataset[nome_saida] = dataset[col1] + dataset[col2]
#     self.set_interface(name='result', value={'dataset': dataset,
#                                             'column':nome_saida,
#                                             'value':dataset[nome_saida]})


# def sum_block():
#     sum_block = Block(name='Soma')
#     sum_block.add_input(name='col1')
#     sum_block.add_input(name='col2')
#     sum_block.add_output(name='result')
#     sum_block.add_compute(sum_func)
#     session.blocks.append(sum_block)


# def bump_block():
#     if 'bump_dict' not in session:
#         session['bump_dict'] = {}
#     block = Block(name='Bump')
#     block.add_input(name='bump col')
#     block.add_input(name='mtm col')
#     block.add_option(name='valor', type='number', value=0.1)
#     block.add_option(name='ordem', type='integer', value=1)
#     block.add_compute(bump_block_func)
#     session.blocks.append(block)


# def bump_block_func(self):
#     nome_saida = self._name
#     bump_col = self.get_interface(name='bump col')['column']
#     mtm_col = self.get_interface(name='mtm col')['column']
#     dataset = self.get_interface(name='bump col')['dataset']
#     value = self.get_option(name='valor')
#     value = float(value)
#     order = self.get_option(name='ordem')
#     order = int(order)

#     if 'order_of_bumping' not in session:
#         session['order_of_bumping'] = 1

#     bump_name = f'bump_{nome_saida}'
#     # breakpoint()
#     if bump_name not in session['bump_dict']:
#         print('=======cache para bump:', bump_col)
#         session['bump_dict'][bump_name] = {'bump_column': bump_col,
#                                             'bump_value': value,
#                                             'mtm_column': mtm_col,
#                                             'mtm_orig': dataset[mtm_col],
#                                             'status': False,
#                                             'mtm_bumped': "Not bumped",
#                                             'order': order}
#         # st.rerun()
    

#     if session['bump_dict'][bump_name]['status']:
#         print('===========compiling bump result for', bump_name)
#         utils.compile_bumps(bump_names=[bump_name])
    