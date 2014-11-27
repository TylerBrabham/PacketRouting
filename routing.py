"""Network routing algorithms.

Package contains implementations of packet routing algorithms from Mitzenmacher
and Upfal.

A node is represented as an array.


TODO:
  - Use a good example to show how much slowdown there can be.
"""

class Network():

  def __init__(self, dimension, restrictions):
    pass

  def bit_fix(self, start, destination, method='naive'):
    pass

class HyperCubeNetwork(Network):
  
  def __init__(self, dimension, restrictions, packets, queues):
    self.dimension = dimension
    self.restrictions = restrictions
    self.packets = packets
    self.queues = queues

  def bit_fix(self, start, destination, method='naive'):
    if method == 'naive':
      return self._bit_fix(start, destination)

  def _bit_fix(self, start, destination):
    number_steps = 0
    for i in range(len(start)):
      if start[i] != destination[i]:
        start[i] = destination[i]
        number_steps += 1
    return number_steps

class ButterflyNetwork(Network):
  pass

def main():
  pass

if __name__ == "__main__":
  main()

