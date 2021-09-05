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

def findRoots(coefficients, start=-10, end=10, step=1):

  func = getFunction(coefficients)

  res = []

  for i in range(start, end, step):
    if func(i) == 0:
      res.append(i)

  return res


print(findRoots([1, 5, 3, 6, 7]))