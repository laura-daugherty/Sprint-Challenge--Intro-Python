class GroundVehicle():
  def __init__(self, num_wheels=4):
    self.num_wheels = num_wheels

  def drive(self):
    return("vroooom")

class Motorcycle(GroundVehicle):
  def __init__(self):
    self.num_wheels = 2

  def drive(self):
    return("BRAAAP!!")

# vehicles = [
#   GroundVehicle(),
#   GroundVehicle(),
#   Motorcycle(),
#   GroundVehicle(),
#   Motorcycle(),
# ]
