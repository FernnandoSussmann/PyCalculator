from Operation import *

def convertInputValue(variableType,inputText):
    return variableType(raw_input(inputText))

def setValues(operation):
    operation.setOperationType(convertInputValue(int,"Insert 1 to add, 2 subtract, 3 multiply, 4 divide, 5 power, 6 root, 7 simple derivative, 8 simple integral\n"))
    operation.setValue1(convertInputValue(float,"\nInsert value 1: "))
    operation.setValue2(convertInputValue(float,"Insert value 2: "))

def selectOperation(operation):
    if (operation.getOperationType() == 1):
      operation.setResult(operation.sumValues())
    elif (operation.getOperationType() == 2):
      operation.setResult(operation.subtractValues())
    elif (operation.getOperationType() == 3):
      operation.setResult(operation.multiplyValues())
    elif (operation.getOperationType() == 4):
      operation.setResult(operation.divideValues())
    elif (operation.getOperationType() == 5):
      operation.setResult(operation.powerOfValue1byValue2())
    elif (operation.getOperationType() == 6):
      operation.setResult(operation.rootOfValue1byValue2())
    elif (operation.getOperationType() == 7):
      operation.setResult(operation.derivativeOfValue1byValue2())
    elif (operation.getOperationType() == 8):
      operation.setResult(operation.integralOfValue1byValue2()) 

def executeOperation(operation):
    setValues(operation)
    selectOperation(operation)
    print(operation)

def main():
  exit = ""
  operation = Operation(0,0,0,0)

  while exit != "n":
      try:
          executeOperation(operation)
      except ValueError:
          print("Invalid Value")
      except OverflowError:
          print("Overflow")
      except ZeroDivisionError:
          print("Value 2 reached a zero division, so we can't calculate")
      finally:
          exit = convertInputValue(str,"\nInsert n to exit, or anything to make another operation\n")

main()
