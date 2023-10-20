import os
import sys
import unittest

parent_directory = os.path.dirname(os.path.abspath(__file__))
project_directory = os.path.dirname(parent_directory)

sys.path.append(project_directory)

from calculadora_estatistica import CalculadoraEstatistica

class TestCalculadoraEstatistica(unittest.TestCase):
    def test_media_lista_vazia(self):
        numeros = []
        resultado = CalculadoraEstatistica.calcular_media(numeros)
        self.assertEqual(resultado, 0.0, "A média de uma lista vazia deve ser 0.")

    def test_media_numeros_positivos(self):
        numeros = [10, 20, 30, 40, 50]
        resultado = CalculadoraEstatistica.calcular_media(numeros)
        self.assertEqual(resultado, 30.0, "A média dos números positivos deve ser 30.")

    def test_media_mistura_numeros(self):
        numeros = [-5, 10, 0, 25, -10]
        resultado = CalculadoraEstatistica.calcular_media(numeros)
        self.assertEqual(resultado, 4.0, "A média de números mistos deve ser 4.")

if __name__ == '__main__':
    unittest.main()
