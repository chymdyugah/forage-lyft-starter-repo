from tyre.tyre import Tyre


class OctoprimeTyre(Tyre):
    def __init__(self, numbers:list):
        self.numbers = numbers
    
    def needs_service(self):
        return sum(self.numbers) >= 3