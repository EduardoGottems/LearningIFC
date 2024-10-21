import unittest
from teste import somar, subrtrair, dividir

class TesteCalculadora(unittest.TestCase):

    def test_somar(self):
        self.assertEqual(somar(5,3),8)
        self.assertEqual(somar(-1,1),0)
        print("Soma OK")

    def test_subtrair(self):
        self.assertEqual(subrtrair(10,5),5)
        print("Subtração OK")

    def test_dividir(self):
        self.assertEqual(dividir(10,2),5)
        with self.assertRaises(ValueError):
            dividir(10,0)
        print("Divisão OK")

if __name__ == '__main__':
    unittest.main()
