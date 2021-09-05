class RootContainer:
  def __init__(self, factor: int, factors: list) -> None:
    self.factor = factor
    self.factors = factors

def getFunction(coefficients: list):

  # 1,2,3 -> x^2 + 2x + 3

  def func(x):
    res = 0
    end = len(coefficients) - 1
    for i in coefficients:
      res += (x ** end) * i
      end -= 1

    return res

  return func

def factorize(num):
  factors = []

  for i in range(1, num + 1):
    if num % i == 0:
      factors.append(i)

  return factors

def findRootsWell(coefficients):
  a = factorize(coefficients[0])
  b = factorize(coefficients[-1])

  print(a)
  print(b)

  possibleRoots: list[RootContainer] = []
  actualRoots = []

  func = getFunction(coefficients)

  for i in a:
    possibleRoots.append(RootContainer(i, b))

  for possibleRoot in possibleRoots:
    for i in possibleRoot.factors:
      if func(i/possibleRoot.factor) == 0:
        actualRoots.append(i/possibleRoot.factor)
      elif func(-i/possibleRoot.factor) == 0:
        actualRoots.append(-i/possibleRoot.factor)
    

  return actualRoots

def findRootsFast(coefficients, start=-10, end=10, step=1):

  func = getFunction(coefficients)

  res = []

  for i in range(start, end, step):
    if func(i) == 0:
      res.append(i)

  return res


print(findRootsWell([1, -4, 3]))