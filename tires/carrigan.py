from tires.tires import Tires

class Carrigan(Tires):
  def __init__(self, tire_wear_sensors):
    self._tire_wear_sensors = tire_wear_sensors

  def needs_service(self):
    for val in self._tire_wear_sensors:
      if val >= 0.9:
        return True
    return False