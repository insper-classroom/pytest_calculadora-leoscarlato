import pytest
import numpy as np
from matematica.Calculadora import soma, sub, multiplicacao, divisao, media_lista_valores


@pytest.mark.op_simples
@pytest.mark.positivos
def test_soma_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    assert 12 == soma(v1,v2)

@pytest.mark.op_simples
def test_soma_um_valor_positivo_um_negativo():
    v1 = 5.0
    v2 = -7.0
    assert -2 == soma(v1,v2)

@pytest.mark.op_complexas
def test_media_lista_positivos():
    assert 3.5 == media_lista_valores([1, 2, 3, 4, 5, 6])



#Exercicio de aula
@pytest.mark.divisao
def test_divisao():
    v1 = 5.0
    v2 = 0.0

    assert divisao(v1,v2) == np.inf


@pytest.mark.media
def test_media():
    lista = [2,4, 'a']
    assert 3 == media_lista_valores(lista)

    
