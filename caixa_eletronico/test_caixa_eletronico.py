import unittest
from caixa_eletronico import CaixaEletronico as ce

class TestCaixaEletronico(unittest.TestCase):

    def test_saque(self):
       
       cedulas = ce.sacar(valor_saque=780)

       self.assertEqual(cedulas, [200, 200, 200, 100, 50, 20, 10])

       print(f"\n\nNotas recebidas: {cedulas}\n\n")

if __name__ == '__main__':
    unittest.main()