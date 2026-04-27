def validar_cpf(cpf):
    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:
        return False
    