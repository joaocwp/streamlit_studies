from streamlit import session_state as session
from Barfi import Block
from Backend import get_execution
from copy import deepcopy


def init(fluxos):
    session['fluxos_custom_blocks'] = fluxos
    for fluxo in fluxos:
        custom_block(fluxo)

def get_dict_from_interfaces(interface):
    aux = {}
    for i in interface:
        aux[i[0]] = i[1]
    return aux


def encode_dict_to_interface(aux_dict):
    interface = [[key, aux_dict[key]] for key in aux_dict]
    return interface


def encode_val_to_entradas(entra, val_dict):
    aux = entra.copy()
    for entrada in aux:
        name = entrada['name']
        tmp = get_dict_from_interfaces(entrada['interfaces'])
        tmp['entrada']['value'] = val_dict[name]
        encoded_interface = encode_dict_to_interface(tmp)
        entrada['interfaces'] = encoded_interface
    return aux

def get_ids_entradas(entradas):
    aux = entradas.copy()
    ids = []
    for entrada in aux:
        tmp = get_dict_from_interfaces(entrada['interfaces'])
        ids.append(tmp['entrada']['id'])
    return ids


def get_ids_from_conn(connections, to_ids):
    aux = connections.copy()
    entry_dict = {}
    ids = []
    ids_from = []
    pos = []
    for i, conn in enumerate(connections):
        if conn['to'] in to_ids:
            entry_dict[i] = {'id': conn['id'],
                             'from': conn['from'],
                             'to': conn['to']}
    return entry_dict


def encode_entradas_to_const(entra, val_dict, custom_name):
    aux = entra['nodes'].copy()
    for entrada in aux:
        name = entrada['name']
        if name in val_dict:
            entrada['type'] = 'dummy'
            entrada['options'] = [['valor', val_dict[name]]]
            tmp = get_dict_from_interfaces(entrada['interfaces'])
            del tmp['entrada']
            encoded_interface = encode_dict_to_interface(tmp)
            entrada['interfaces'] = encoded_interface
    for block in aux:
        block['name'] = block['name'] + f'_{custom_name}'


def get_to_dict_from_conn(connection):
    aux = {i['to']:i for i in connection}
    return aux


def encode_conn_from_dict(dict_conn):
    return list(dict_conn.values())


def delete_connections(fluxo, to_ids):
    tmp = get_to_dict_from_conn(fluxo['connections'])
    for i in to_ids:
        try:
            del tmp[i]
        except:
            pass
    return tmp


def get_entradas(fluxo):
    entradas = [i for i in fluxo['nodes'] if i['type'] == 'entrada']
    return entradas


def get_fluxo_const(fluxo, val_dict, nome_custom):
    aux_fluxo = deepcopy(fluxo)
    saidas = [i for i in aux_fluxo['nodes'] if i['type'] == 'saida']
    saida_names = [i['name'] for i in saidas]
    entradas = [i for i in aux_fluxo['nodes'] if i['type'] == 'entrada']
    entrada_names = [i['name'] for i in entradas]
    ids_entradas = get_ids_entradas(entradas)
    entry_conn = get_ids_from_conn(aux_fluxo['connections'], ids_entradas)
    tmp = delete_connections(aux_fluxo, ids_entradas)
    aux_fluxo['connections'] = encode_conn_from_dict(tmp)
    encode_entradas_to_const(aux_fluxo, val_dict, nome_custom)
    return aux_fluxo, entrada_names, saida_names


def custom_block(nome_fluxo):
    # breakpoint()
    print("Criando custom:", nome_fluxo)
    fluxo = session['fluxos_custom_blocks'][nome_fluxo]
    block = Block(name=nome_fluxo)
    __, entrada_names, saida_names = get_fluxo_const(fluxo, {}, '')
    for entrada in entrada_names:
        block.add_input(name=entrada)
    for saida in saida_names:
        block.add_output(name=saida)
    block.add_compute(custom_block_func)
    session.blocks.append(block)


def custom_block_func(self):
    nome_fluxo = self._type
    nome_bloco = self._name
    print("Executando custom:", nome_fluxo)
    fluxo = session['fluxos_custom_blocks'][nome_fluxo]
    val_dict = {}
    for entrada in self._inputs:
        val_dict[entrada] = self.get_interface(name=entrada)
    fluxo_encodado, __, __ = get_fluxo_const(fluxo, val_dict, nome_bloco)
    get_execution(fluxo_encodado, nome_bloco)
    for saida in self._outputs:
        val = session['saida_dict'][f'{saida}_{nome_bloco}']
        self.set_interface(name=saida, value=val)
