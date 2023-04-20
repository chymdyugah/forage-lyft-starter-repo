import unittest

from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine


class EngineTestCase(unittest.TestCase):
    def test_capulet_engine(self):
        engine = CapuletEngine(200, 100)
        self.assertFalse(engine.needs_service())
    
    def test_willoughby_engine(self):
        engine = WilloughbyEngine(100000, 30000)
        self.assertTrue(engine.needs_service())
    
    def test_sternman_engine(self):
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())
