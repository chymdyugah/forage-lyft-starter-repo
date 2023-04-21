import unittest

from tyre.carrigan import CarriganTyre
from tyre.octoprime import OctoprimeTyre


class TyreTestCase(unittest.TestCase):
    def test_carrigan_tyre(self):
        tyre = CarriganTyre([0, 0.9, 0.4, ])
        self.assertTrue(tyre.needs_service())

    
    def test_octprime_tyre(self):
        tyre = OctoprimeTyre([0, 0.9, 0.4, 1])
        self.assertFalse(tyre.needs_service())
