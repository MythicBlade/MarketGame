from Investment import *

class stock(Investment):
    def __init__(self,name: str, value: float, description: str):
        super().__init__(name, value, description)