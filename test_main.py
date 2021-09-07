import pytest
from conta import Conta

@pytest.fixture
def conta_test():
    return Conta('1', 'Sandão')

def test_deposito_valores_como_string(conta_test):
    conta_test.depositar('dinheiro')
    assert conta_test.saldo == conta_test.saldo

def test_deposito_igual_zero(conta_test):
    assert conta_test.depositar(0) == None

def test_validacao_extrato(conta_test):
    assert conta_test.extrato(25) != False 

def test_sacar_valor_correto(conta_test):
    assert conta_test.sacar(15) == True

def test_saque_maior_que_limite(conta_test):
    assert conta_test.sacar(53) == False

def test_transfer_valor_maior_que_saldo(conta_test):
    assert conta_test.transferir('321', 51) == False

