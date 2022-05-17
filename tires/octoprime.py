from tires.tires import Tires

class Octoprime(Tires):
  def __init__(self, tire_wear_sensors):
    self._tire_wear_sensors = tire_wear_sensors

  def needs_service(self):
    sensor_val_sum = sum(self._tire_wear_sensors)
    if sensor_val_sum >= 3:
      return True
    return False