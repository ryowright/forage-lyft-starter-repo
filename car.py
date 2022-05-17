from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine, battery, tires):
        self._engine = engine
        self._battery = battery
        self._tires = tires

    def needs_service(self):
        return self._engine.needs_service() or self._battery.needs_service() or self._tires.needs_service()
