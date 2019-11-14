class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # pass
    self.current
    if self.current < self.capacity:
      self.storage[self.current] = item
      self.current += 1
    elif self.current == self.capacity:
      self.storage[0] = item
      self.current += 1
    else:
      self.storage[self.current - self.capacity] = item
      self.current += 1

  def get(self):
    # pass
    return list(filter(None, self.storage))