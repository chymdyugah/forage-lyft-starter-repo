from tyre.tyre import Tyre

class CarriganTyre(Tyre):
    def __init__(self, numbers:list):
        self.numbers = numbers
    
    def needs_service(self):
        for i in self.numbers:
            if i >= 0.9:
                return True
        return False