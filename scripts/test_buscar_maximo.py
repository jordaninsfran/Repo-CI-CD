from buscar_maximo import get_maximo
import pytest

def test():
	valores = [3,2,1,4,5,10,300]
	assert get_maximo(valores) == 310
