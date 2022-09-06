from programa1 import sumar
import pytest

def test1():
    assert sumar(2,3) == 5
def test2():
    assert sumar(3,1) == 2 # ERROR INTENCIONAL.
