exit = ""

while exit != "n":
    operation = raw_input("Insert 1 to add, 2 subtract, 3 multiply, 4 divide, 5 power, 6 root, 7 simple derivative, 8 simple integral\n")
    value1 = raw_input("Insert value 1: ")
    value2 = raw_input("Insert value 2: ")

    try:
        operation = int(operation)
        value1 = float(value1)
        value2 = float(value2)

        result = 0
        if (operation == 1):
            result = value1 + value2
        elif (operation == 2):
            result = value1 - value2
        elif (operation == 3):
            result = value1 * value2
        elif (operation == 4 and value2 != 0):
            result = value1 / value2
        elif (operation == 5):
            result = value1 ** value2
        elif (operation == 6 and  value2 != 0):
            result = value1 ** (1/value2)
        elif (operation == 7):
            result = value1 *value2
            value2 -= 1
            print("\n" + str(result) + "x^" + str(value2) + "\n")
        elif (operation == 8 and value2 != -1):
            result = value1 /(value2 + 1)
            value2 += 1 
            print("\n" + str(result) + str("x^") + str(value2) + "\n")
        else:
            print("Ivalid Operation\n")

        print(result)

    except ValueError:
        print("Invalid Value")
    except OverflowError:
        print("Overflow")
    exit = raw_input("\nInsert n to exit, or anything to make another operation\n")
