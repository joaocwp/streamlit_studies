from barfi import Block

def init():
    return add5block()

def add5block():
    block = Block(name='add5')
    block.add_input(name='entrada')
    block.add_output(name='saida')
    block.add_compute(add5func)
    return block

def add5func(self):
    valor = self._inputs['entrada'] + 5
    self.set_interface(name='saida', value=valor)
