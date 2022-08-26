import numpy as np

def soma(va: float, vb: float):
    ''' Função que retorna a soma entre dois valores
    '''
    return va + vb

def sub(va: float, vb: float):
    ''' Função que retorna a subtração entre dois valores
    '''
    return va - vb

def multiplicacao(va: float, vb: float):
    ''' Função que retorna a multiplicação entre dois valores
    '''
    return va * vb

def divisao(va: float, vb: float):
    ''' Função que retorna a divisão entre dois valores
    '''

    if vb != 0:
        return va / vb
    else:
        return np.inf

def media_lista_valores(v:list):
    ''' Função que retorna a média entre N valores
    '''

    if len(v) > 0:
        lista_valores = []
        for valor in v:
            if isinstance(valor, int or float):
                lista_valores.append(valor)
        return np.mean(lista_valores)
    return 0
