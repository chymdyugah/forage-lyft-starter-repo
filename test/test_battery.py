import unittest
from datetime import date

from battery.splindler import SplindlerBattery
from battery.nubbin import NubbinBattery


class BatteryTestCase(unittest.TestCase):
    def test_splindler(self):
        battery = SplindlerBattery(date(2022, 1, 1), date.today())
        self.assertFalse(battery.needs_service())
    
    def test_nubbin(self):
        battery = NubbinBattery(date(2020, 1, 1), date.today())
        self.assertFalse(battery.needs_service())

