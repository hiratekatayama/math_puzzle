class MinStack(object):
  def __init__(self):
    self.items = []

  def push(self, x):
    return self.items.append(x)

  def pop(self):
    return self.items.pop()

  def top(self):
    return max(self.items)

  def getMin(self):
    return min(self.items)

  def getList(self):
    return self.items

class MinStack(object):
  def __init__(self):
    self.items = []

  def push(self, x):
    curMin = self.getMin()
    if curMin == None or x < curMin:
      curMin = x
    self.items.append((x, curMin))

  def pop(self):
    return self.items.pop()

  def top(self):
    if len(self.q) == 0:
      return None
    else:
      return self.items[len(self.items) - 1][0]

  def getMin(self):
    if len(self.items) == 0:
      return None
    else:
      return self.items[len(self.items) - 1][1]

if __name__ == '__main__':
  minstack = MinStack()

  minstack.push(-2)
  minstack.push(0)
  minstack.push(-3)
  print(minstack.getMin())
  #print(minstack.pop())
  print(minstack.top())
  #print(minstack.getMin())

  print(minstack.getList())
