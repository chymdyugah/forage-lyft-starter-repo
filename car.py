from abc import ABC, abstractmethod
from datetime import date

from engine.engine import Engine
from battery.battery import Battery

from battery.nubbin import NubbinBattery
from battery.splindler import SplindlerBattery

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass


class Car(Serviceable):
    def __init__(self, battery:Battery, engine:Engine):
        self.battery = battery
        self.engine = engine

    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service()


class CarFactory:
    def create_calliope(self, current_date:date, last_service_date:date, current_mileage:int, last_service_mileage:int):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SplindlerBattery(last_service_date, current_date)
        car = Car(battery=battery, engine=engine)
        return car
    
    def create_glissade(self, current_date:date, last_service_date:date, current_mileage:int, last_service_mileage:int):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SplindlerBattery(last_service_date, current_date)
        car = Car(battery=battery, engine=engine)
        return car
    
    def create_palindrome(self, current_date:date, last_service_date:date, warning_ligh_is_ont:bool):
        engine = SternmanEngine(warning_light_is_on=warning_ligh_is_ont)
        battery = SplindlerBattery(last_service_date, current_date)
        car = Car(battery=battery, engine=engine)
        return car
    
    def create_rorschach(self, current_date:date, last_service_date:date, current_mileage:int, last_service_mileage:int)->Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(battery=battery, engine=engine)
        return car
    
    def create_thovex(self, current_date:date, last_service_date:date, current_mileage:int, last_service_mileage:int)->Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(battery=battery, engine=engine)
        return car
    
