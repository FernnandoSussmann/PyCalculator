class Operation(object):
  def __init__(self,operationType, value1, value2, result):
    self.operationType = operationType
    self.value1 = value1
    self.value2 = value2
    self.result = result

  def getOperationType(self):
    return self.operationType

  def getValue1(self):
    return self.value1

  def getValue2(self):
    return self.value2

  def getResult(self):
    return self.result

  def setOperationType(self, operationType):
    self.operationType = operationType

  def setValue1(self, value1):
    self.value1 = value1

  def setValue2(self, value2):
    self.value2 = value2

  def setResult(self, result):
    self.result = result

  def sumValues(self):
    return self.getValue1() + self.getValue2()

  def subtractValues(self):
    return self.getValue1() - self.getValue2()  

  def multiplyValues(self):
    return self.getValue1() * self.getValue2() 

  def divideValues(self):
    return self.getValue1() / self.getValue2()

  def powerOfValue1byValue2(self):
    return self.getValue1() ** self.getValue2()

  def rootOfValue1byValue2(self):
    return self.getValue1() ** (1/self.getValue2())

  def derivativeOfValue1byValue2(self):
    result = self.getValue1() * self.getValue2()
    self.setValue2(self.getValue2() -1)
    return result

  def integralOfValue1byValue2(self):
    self.setValue2(self.getValue2() + 1)
    result = self.getValue1() / self.getValue2()
    return result

  def __str__(self):
    if self.getOperationType() in range(1,7):
      return str(self.getResult())
    elif self.getOperationType() in (7,8):
      return "\n" + str(self.getResult()) + "x^" + str(self.getValue2()) + "\n"
    else:
      return "Invalid Operation"
