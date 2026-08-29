from src.calculadora import Calculadora


def test_somar():
    calc = Calculadora()
    assert calc.somar(2, 3) == 5