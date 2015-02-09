import unittest
from caixa import caixa_eletronico

class TestCaixa(unittest.TestCase):

    def test_um_real(self):
        self.assertEquals(caixa_eletronico(1), None)

    def test_dois_reais(self):
        self.assertEquals(caixa_eletronico(2), { 2 : 1, 5 : 0, 10 : 0, 20 : 0, 50 : 0, 100 : 0})

    def test_cinco_reais(self):
        self.assertEquals(caixa_eletronico(5), { 2 : 0, 5 : 1, 10 : 0, 20 : 0, 50 : 0, 100 : 0})

    def test_seis_reais(self):
        self.assertEquals(caixa_eletronico(6), { 2 : 3, 5 : 0, 10 : 0, 20 : 0, 50 : 0, 100 : 0})

    def test_sete_reais(self):
        self.assertEquals(caixa_eletronico(7), { 2 : 1, 5 : 1, 10 : 0, 20 : 0, 50 : 0, 100 : 0})

    def test_nove_reais(self):
        self.assertEquals(caixa_eletronico(9), { 2 : 2, 5 : 1, 10 : 0, 20 : 0, 50 : 0, 100 : 0})

    def test_dez_reais(self):
        self.assertEquals(caixa_eletronico(10), { 2 : 0, 5 : 0, 10 : 1, 20 : 0, 50 : 0, 100 : 0})

    def test_onze_reais(self):
        self.assertEquals(caixa_eletronico(11), None)

    def test_vinte_reais(self):
        self.assertEquals(caixa_eletronico(20), { 2 : 0, 5 : 0, 10 : 0, 20 : 1, 50 : 0, 100 : 0})

    def test_cinquenta_reais(self):
        self.assertEquals(caixa_eletronico(50), { 2 : 0, 5 : 0, 10 : 0, 20 : 0, 50 : 1, 100 : 0})

    def test_cem_reais(self):
        self.assertEquals(caixa_eletronico(100), { 2 : 0, 5 : 0, 10 : 0, 20 : 0, 50 : 0, 100 : 1})

    def test_cento_e_oitenta_e_sete_reais(self):
        self.assertEquals(caixa_eletronico(187), { 2 : 1, 5 : 1, 10 : 1, 20 : 1, 50 : 1, 100 : 1})

    def test_mil_reais(self):
        self.assertEquals(caixa_eletronico(1000), { 2 : 0, 5 : 0, 10 : 0, 20 : 0, 50 : 0, 100 : 10})

#    def test_mil_e_quarenta_e_oito_reais(self):
#        self.assertEquals(caixa_eletronico(1048), { 2 : 4, 5 : 0, 10 : 0, 20 : 2, 50 : 0, 100 : 10})

unittest.main()
