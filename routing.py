"""Network routing algorithms.

Package contains implementations of packet routing algorithms from Mitzenmacher
and Upfal.

A node is represented as an array.


TODO:
  - Use a good example to show how much slowdown there can be. Could make all
    packets start at the same place and end at the same place, showing that the
    random scheme gives significant improvement.

  - Could try a bit fixing strategy that just randomizes which bit to fix. Some
    packets won't move during an iteration then. Only allows you to sample from
    n things, as opposed to 2^n things.
"""


class Network():

  def bit_fix(self, start, destination, method='naive'):
    pass


class Packet():

  def __init__(self, location):
    # Current position of the given packet.
    self.location = location

    # Current bit that needs to be processed.
    self.current_bit = 0

    # Number of steps it took to reach destination
    self.number_steps = 0

  def increment_bit(self):
    self.current_bit += 1

  def increment_number_steps(self):
    self.number_steps += 1


class HyperCubeNetwork(Network):
  
  def __init__(self, dimension, restrictions=[]):
    self.dimension = dimension
    self.restrictions = restrictions

    # Queues are used to determine which packet should be allowed to move next.
    # Queues are FIFO.
    self._queues = {}

  def _clear_empty_queues():
    pass

  def route_packets(self, packets, destinations):
    # Either iterate over packets, or iterate over the queues and only pull from
    # the front of the queue.
    pass

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
  dimension = 8
  packets = [Packet("0" * dimension)]
  destinations = ["1" * dimension]

  network = HyperCubeNetwork(dimension)
  print network.route_packets(packets, destinations)


if __name__ == "__main__":
  main()

