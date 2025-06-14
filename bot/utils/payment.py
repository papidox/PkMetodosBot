
# payment.py
pix_keys = ["pix@1.com", "pix@2.com", "pix@3.com"]
from random import choice

def chave_pix_ativa():
    return choice(pix_keys)

def gerar_codigo_pagamento(usuario):
    from random import randint
    codigo = f"{usuario[:3].upper()}{randint(100,999)}BOT"
    return codigo
