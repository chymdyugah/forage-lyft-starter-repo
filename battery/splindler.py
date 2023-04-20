from battery.battery import Battery
from datetime import date

class SplindlerBattery(Battery):
    def __init__(self, battery_last_service_date:date, current_date:date):
        self.battery_last_service_date = battery_last_service_date
        self.current_date = current_date
    
    def needs_service(self):
        service_threshold_date = self.battery_last_service_date.replace(year=self.battery_last_service_date.year + 2)
        print(service_threshold_date)
        return service_threshold_date < self.current_date
