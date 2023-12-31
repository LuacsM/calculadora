import unittest
from calculadora_estatistica import CalculadoraEstatistica

class CustomTextTestResult(unittest.TextTestResult):
    def addSuccess(self, test):
        super(CustomTextTestResult, self).addSuccess(test)
        self.stream.writeln(f'Success: {test.id()}')

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
    runner = unittest.TextTestRunner(resultclass=CustomTextTestResult)
    unittest.main(testRunner=runner)
