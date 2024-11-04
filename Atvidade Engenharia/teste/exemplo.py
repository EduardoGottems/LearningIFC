import src.Conversao as Conversao
import unittest

class TestConversao(unittest.TestCase):
    
    def test_binarioToDecimal(self):
        self.assertEqual(Conversao.binario_para_decimal_ipv4("11111111.11111111.11111111.11111111"),"255.255.255.255")
        self.assertEqual(Conversao.binario_para_decimal_ipv4("00000000.00000000.00000000.00000000"),"0.0.0.0")
        print("Binario para decimal ok!")

    def test_decimalToBinario(self):
        self.assertEqual(Conversao.decimal_para_binario_ipv4("255.255.255.255"),"11111111.11111111.11111111.11111111")
        self.assertEqual(Conversao.decimal_para_binario_ipv4("0.0.0.0"),"00000000.00000000.00000000.00000000")
        print("Decimal para binario ok!")

    def error_0bTo10b(self):
        self.assertRaises(ValueError, Conversao.binario_para_decimal_ipv4 , "11111111.11111111.11111111.111111111111111111")
        self.assertRaises(ValueError, Conversao.binario_para_decimal_ipv4 , "batata.00000000.00000000.00000000")        
        print("Conversao com caracteres fora da base ok!")
    
    def error_10bTo0b(self):
        self.assertRaises(ValueError, Conversao.decimal_para_binario_ipv4, "256.255.255.255" )
        self.assertRaises(ValueError, Conversao.decimal_para_binario_ipv4, "sas.255.255.255" )
        print("Conversao com caracteres fora da base ok!")