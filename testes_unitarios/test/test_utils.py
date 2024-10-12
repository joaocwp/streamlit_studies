from unittest.mock import MagicMock, patch, Mock
import unittest
import sys

ses_dict = {'config':{'bump1':{'order':1},
                          'bump2':{'order':2},}}
mock = MagicMock()
mock.session_state = ses_dict
mock.cache_data.return_value = lambda x: x #funciona sem também
@patch.dict('sys.modules', {'streamlit': mock,
                            'math_util':MagicMock(),
                            'beholder': MagicMock()})
def test_get_max_order():
    from src.utils import get_max_order
    assert get_max_order() == 2

ses_dict = {'config':{'bump1':{'order':1},
                          'bump2':{'order':2},}}
mock = MagicMock()
mock.session_state = ses_dict
mock.cache_data.return_value = lambda x: x #funciona sem também
@patch.dict('sys.modules', {'streamlit': mock,
                            'math_util':MagicMock(),
                            'beholder': MagicMock()})
class TestSt(unittest.TestCase):

   def test_fix_max_order(self):
        from src.utils import fix_max_order, get_max_order
        fix_max_order()
        assert get_max_order() == 1


mock = MagicMock()
mock.session_state = {}
@patch.dict('sys.modules', {'streamlit': mock,
                            'math_util':MagicMock(),
                            'beholder': MagicMock()})
def test_get_max_order0():
    from src.utils import get_max_order
    assert get_max_order() == 0

def test_get_addition():
    mock = MagicMock()
    mock.session_state = {'config':{'bump1':{'order':1},
                          'bump2':{'order':3},}}
    mock.cache_data.return_value = lambda x: x #Aqui é necessário p/ testar funcao com cache
    with patch.dict('sys.modules', {'streamlit': mock,
                                    'math_util': mock,
                                    'beholder':mock}):
        from src.utils import get_addition
        get_addition()
        mock.add.return_value = 2
        assert get_addition() == 2
        mock.add.assert_called()


mock = MagicMock()
mock.cache_data.return_value = lambda x: x
mock.multiply.return_value = 1
@patch.dict('sys.modules', {'streamlit':mock,
                            'math_util':mock,
                            'beholder':mock})
def test_get_multiplication():
    from src.utils import get_multiplication
    assert get_multiplication() == 1
    # mock.multiply.assert_called() #não funciona, não tem acesso ao obj mock

def test_get_multiplication2():
    mock = MagicMock()
    mock.multiply.return_value = 1
    mock.cache_data.return_value = lambda x: x
    with patch.dict('sys.modules', {'streamlit':mock,
                                    'math_util':mock,
                                    'beholder':mock}):
        from src.utils import get_multiplication
        assert get_multiplication() == 1
        mock.multiply.assert_called()



mock = MagicMock()    
@patch.dict('sys.modules', {'math_util': mock,
                            'beholder':mock,
                            'streamlit': MagicMock()})
class TestMath(unittest.TestCase):
    def test_get_subtraction(self):
        from src.utils import get_subtraction
        mock.subtract.return_value = 0
        assert get_subtraction() == 0
        mock.subtract.assert_called()

    # def test_get_multiplication(self):
    #     from src.utils import get_multiplication
    #     mock.multiply.return_value = 1
    #     assert get_multiplication() == 1
    #     mock.multiply.assert_called()   

@patch.dict('sys.modules', {'beholder': MagicMock()})
class TestMath2(unittest.TestCase):
    def test_get_subtraction(self):
        from src.math_util import subtract
        assert subtract(1, 2) == -1
        assert subtract(2, 1) == 1
    
    def test_get_multiplication(self):
        from src.math_util import multiply
        assert multiply(1, 2) == 2
        assert multiply(2, -1) == -2
    
    def test_get_addition(self):
        from src.math_util import add
        assert add(1, 2) == 3
        assert add(2, -1) == 1

# mock = MagicMock()    
# @patch.dict('sys.modules', {"math_util", mock})    
# def test_get_multiplication(mock_math):
#     from src.utils import get_multiplication
#     mock_math.return_value = 2
#     assert get_multiplication() == 2    