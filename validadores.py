import re

def email_valido(email: str) -> bool:
    regex = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    return bool(regex.fullmatch(email.strip()))

def cpf_valido(cpf: str) -> bool:
    cpf = re.sub(r'\D', '', cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    def calc_digito(cpf_parcial, peso):
        soma = sum(int(digito) * p for digito, p in zip(cpf_parcial, range(peso, 1, -1)))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)

    d1 = calc_digito(cpf[:9], 10)
    d2 = calc_digito(cpf[:9] + d1, 11)
    return cpf.endswith(d1 + d2)

def telefone_valido(telefone: str) -> bool:
    telefone = telefone.strip()
    #Código de país seguido do número, 10 a 14 dígitos
    regex = re.compile(r"^\+\d{1,3}\d{10,14}$")
    return bool(regex.fullmatch(telefone))
