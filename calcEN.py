from Operation import *

def convert_input_value(variable_type,input_text):
    return variable_type(raw_input(input_text))

def set_values(operation):
    operation.set_operation_type(convert_input_value(int,"Insert 1 to add, 2 subtract, 3 multiply, 4 divide, 5 power, 6 root, 7 simple derivative, 8 simple integral\n"))
    operation.set_value1(convert_input_value(float,"\nInsert value 1: "))
    operation.set_value2(convert_input_value(float,"Insert value 2: "))

def select_operation(operation):
    operations = [operation.sum_values(), operation.subtract_values(), operation.multiply_values(), operation.divide_values(), 
                 operation.power_of_value1_by_value2(), operation.root_of_value1_by_value2(), operation.derivative_of_value1_by_value2(), 
                 operation.integral_of_value1_by_value2()]
    operation.set_result(operations[operation.get_operation_type() - 1])

def execute_operation(operation):
    set_values(operation)
    select_operation(operation)
    operation.adjust_value2()
    print(operation)

def main():
  exit = ""
  operation = Operation(0,0,0,0)

  while exit != "n":
      try:
          execute_operation(operation)
      except ValueError:
          print("Invalid Value")
      except OverflowError:
          print("Overflow")
      except ZeroDivisionError:
          print("Value 2 reached a zero division, so we can't calculate")
      finally:
          exit = convert_input_value(str,"\nInsert n to exit, or anything to make another operation\n")

main()
