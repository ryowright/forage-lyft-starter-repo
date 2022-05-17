import unittest

from tires.carrigan import Carrigan
from tires.octoprime import Octoprime

class TestCarrigan(unittest.TestCase):
  def test_tires_should_be_serviced(self):
    tires = Carrigan([0.2, 0.5, 0.9, 1.0])
    self.assertTrue(tires.needs_service())
  
  def test_tires_should_not_be_serviced(self):
    tires = Carrigan([0.2, 0.5, 0.3, 0.0])
    self.assertFalse(tires.needs_service())

class TestOctoprime(unittest.TestCase):
  def test_tires_should_be_serviced(self):
    tires = Octoprime([1.0, 1.0, 1.0, 0.4])
    self.assertTrue(tires.needs_service())

  def test_tires_should_not_be_serviced(self):
    tires = Octoprime([0.2, 0.7, 1.0, 0.2])
    self.assertFalse(tires.needs_service())