import re

def cor_valida(cor):
    modelo = '^#([A-Fa-f0-9]{3}|[A-Fa-f0-9]{6}|[A-Fa-f0-9]{4}|[A-Fa-f0-9]{8})$'
    resposta = re.findall(modelo, cor)
    return resposta