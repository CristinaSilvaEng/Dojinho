import unittest
from cheque import cheque_por_extenso

class TestCheque(unittest.TestCase):

    def test_um_centavo(self):
        self.assertEquals(cheque_por_extenso(0.01), 'um centavo')

    def test_dois_centavos(self):
        self.assertEquals(cheque_por_extenso(0.02), 'dois centavos')

unittest.main()
