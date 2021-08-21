import unittest
from troco import troco as tc

class TestTroco(unittest.TestCase):

    def test_troco(self):
       
       troco = tc.pagar(valor_compra=80, valor_pago=100)

       self.assertEqual(troco, [20])

       print(f"\n\nTroco Recebido: {troco}\n\n")

if __name__ == '__main__':
    unittest.main()