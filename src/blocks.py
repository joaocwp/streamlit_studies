from barfi import Block
import streamlit as st
from streamlit import session_state as session
# import utils

print("import blocks")


def init():

    print('starting blocks')
    session.blocks = []
    constant_block()
    saida_block()
    create_df_block()
    sum_block()
    entrada_block()
    div_block()
    mult_block()
    minus_block()
    print_block()
    # result_block()
    # sum_block()
    # bump_block()

def constant_block():
    block = Block(name='constante')
    block.add_option(name='valor', type='number', value=1)
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
    block.add_input(name='valor')
    block.add_output(name='saida')
    block.add_compute(saida_func)
    session.blocks.append(block)


def saida_func(self):
    if 'saida_dict' not in session:
        session.saida_dict = {}
    valor = self.get_interface(name='valor')
    self.set_interface(name='saida', value=valor)
    session['saida_dict'][self._name] = valor
    print('Saida', self._name, ':', valor)


def print_block():
    block = Block(name='print')
    block.add_input(name='valor')
    block.add_output(name='saida')
    block.add_compute(print_func)
    session.blocks.append(block)


def print_func(self):
    valor = self.get_interface(name='valor')
    self.set_interface(name='saida', value=valor)
    print('Saida', self._name, ':', valor)
    session.saida = valor


def create_df_block(name='Input'):
    block = Block(name=name.replace('.','_'))
    dataframe = session.dados
    for col in dataframe:
        block.add_output(name=col, value=dataframe[col])
    block.add_compute(df_block_func)
    session.blocks.append(block)


def sum_block():
    block = Block(name='Soma')
    block.add_input(name='valor 1')
    block.add_input(name='valor 2')
    block.add_output(name='saida')
    block.add_compute(sum_block_func)
    session.blocks.append(block)


def sum_block_func(self):
    val1 = self.get_interface(name='valor 1')
    val2 = self.get_interface(name='valor 2')
    result = val1 + val2
    print("soma:", result)
    self.set_interface(name='saida', value=result)


def minus_block():
    block = Block(name='Subtracao')
    block.add_input(name='valor 1')
    block.add_input(name='valor 2')
    block.add_output(name='saida')
    block.add_compute(mins_block_func)
    session.blocks.append(block)


def mins_block_func(self):
    val1 = self.get_interface(name='valor 1')
    val2 = self.get_interface(name='valor 2')
    result = val1 - val2
    self.set_interface(name='saida', value=result)


def div_block():
    block = Block(name='Divisao')
    block.add_input(name='valor 1')
    block.add_input(name='valor 2')
    block.add_output(name='saida')
    block.add_compute(div_block_func)
    session.blocks.append(block)


def div_block_func(self):
    val1 = self.get_interface(name='valor 1')
    val2 = self.get_interface(name='valor 2')
    result = val1 / val2
    print("div:", result)
    self.set_interface(name='saida', value=result)


def mult_block():
    block = Block(name='Multiplicacao')
    block.add_input(name='valor 1')
    block.add_input(name='valor 2')
    block.add_output(name='saida')
    block.add_compute(mult_block_func)
    session.blocks.append(block)


def mult_block_func(self):
    val1 = self.get_interface(name='valor 1')
    val2 = self.get_interface(name='valor 2')
    result = val1 * val2
    print("mult:", result)
    self.set_interface(name='saida', value=result)


def entrada_block():
    block = Block(name='entrada')
    block.add_input(name='entrada', value=1)
    block.add_output(name='saida')
    block.add_compute(entrada_block_func)
    session.blocks.append(block)


def entrada_block_func(self):
    nome = self._name
    entrada = self.get_interface(name='entrada')
    self.set_interface(name='saida', value=entrada)


def df_block_func(self):
    return
