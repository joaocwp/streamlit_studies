from unittest.mock import MagicMock, patch, Mock
import streamlit_mock
import unittest
import sys
# sys.path.append('src')
#não funciona com cache data
def test_get_max_order():
    sm = streamlit_mock.StreamlitMock()
    session = sm.get_session_state()
    session.update({'config':{'bump1':{'order':1},
                         'bump2':{'order':2},}})
    mock = MagicMock()
    with patch.dict('sys.modules', {'math_util': mock,
                                    'beholder':mock}):
        from src.utils import get_max_order
        assert get_max_order() == 2
        session.update({'config':{'bump1':{'order':1},
                        'bump2':{'order':3},}})
        assert get_max_order() == 3
        session.clear()
        assert get_max_order() == 0


@patch.dict('sys.modules', {'math_util':MagicMock(),
                            'beholder': MagicMock()})
def test_fix_max_order():
    sm = streamlit_mock.StreamlitMock()
    session = sm.get_session_state()
    session.update({'config':{'bump1':{'order':1},
                         'bump2':{'order':2},}})
    from src.utils import fix_max_order, get_max_order
    assert get_max_order() == 2
    fix_max_order()
    assert get_max_order() == 1

def test_get_addition():
    mock = MagicMock()
    with patch.dict('sys.modules', {'math_util': mock,
                                    'beholder':mock}):
        from src.utils import get_addition
        get_addition()
        mock.add.return_value = 2
        assert get_addition() == 2
        mock.add.assert_called()
