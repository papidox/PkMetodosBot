
def chave_pix_ativa():
    return 'pix@pkmetodos.com'

def gerar_codigo_pagamento(usuario, metodo):
    import random
    return f'PXD-{metodo[:5].upper()}-{random.randint(1000,9999)}-@{usuario}'
