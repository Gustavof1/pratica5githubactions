# test_validadores.py

from validadores import email_valido, cpf_valido, telefone_valido

def test_email_valido():
    assert email_valido("exemplo.usuario@gmail.com")

def test_cpf_valido():
    assert cpf_valido("529.982.247-25")

def test_cpf_invalido():
    assert not cpf_valido("111.111.111-11")

def test_telefone_valido():
    assert telefone_valido("+5531999999999")

def test_telefone_invalido():
    assert not telefone_valido("12345678")
