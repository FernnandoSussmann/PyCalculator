class Operation(object):
  def __init__(self,operation_type, value1, value2, result):
    self.operation_type = operation_type
    self.value1 = value1
    self.value2 = value2
    self.result = result

  def get_operation_type(self):
    return self.operation_type

  def get_value1(self):
    return self.value1

  def get_value2(self):
    return self.value2

  def get_result(self):
    return self.result

  def set_operation_type(self, operation_type):
    self.operation_type = operation_type

  def set_value1(self, value1):
    self.value1 = value1

  def set_value2(self, value2):
    self.value2 = value2

  def set_result(self, result):
    self.result = result

  def sum_values(self):
    return self.get_value1() + self.get_value2()

  def subtract_values(self):
    return self.get_value1() - self.get_value2()  

  def multiply_values(self):
    return self.get_value1() * self.get_value2() 

  def divide_values(self):
    return self.get_value1() / self.get_value2()

  def power_of_value1_by_value2(self):
    return self.get_value1() ** self.get_value2()

  def root_of_value1_by_value2(self):
    return self.get_value1() ** (1/self.get_value2())

  def derivative_of_value1_by_value2(self):
    result = self.get_value1() * self.get_value2()
    return result

  def integral_of_value1_by_value2(self):
    result = self.get_value1() / (self.get_value2() + 1)
    return result

  def adjust_value2(self):
    if (self.get_operation_type() == 7):
      self.set_value2(self.get_value2() - 1)
    elif (self.get_operation_type() == 8):
      self.set_value2(self.get_value2() + 1)

  def __str__(self):
    if self.get_operation_type() in range(1,7):
      return str(self.get_result())
    elif self.get_operation_type() in (7,8):
      return "\n" + str(self.get_result()) + "x^" + str(self.get_value2()) + "\n"
    else:
      return "Invalid Operation"
