import pytest
import finanzas

def test_onlynumerics():
    seq = '"3#mar~@iaaa12"'
    resultado = '312'
    assert resultado==finanzas.only_numerics(seq)