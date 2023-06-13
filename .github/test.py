from decimalABinario import decimal_a_binario
import unittest

class DecimalABinarioTest(unittest.TestCase):
    def test_decimal_cero(self):
        resultado = decimal_a_binario(0)
        self.assertEqual(resultado, '0')

    def test_decimal_positivo(self):
        resultado = decimal_a_binario(42)
        self.assertEqual(resultado, '101010')

    def test_decimal_maximo(self):
        resultado = decimal_a_binario(255)
        self.assertEqual(resultado, '11111111')

    def test_decimal_personalizado(self):
        resultado = decimal_a_binario(13)
        self.assertEqual(resultado, '1101')

if __name__ == '__main__':
    unittest.main()













