sair = ""

while sair != "n":
    operacao = raw_input("Digite 1 para soma, 2 subtracao, 3 multiplicacao, 4 divisao, 5 potencia, 6 raiz, 7 derivada simples, 8 integral simples\n")
    valor1 = raw_input("Primeiro valor: ")
    valor2 = raw_input("Segundo valor: ")

    try:
        operacao = int(operacao)
        valor1 = float(valor1)
        valor2 = float(valor2)

        resultado = 0
        if (operacao == 1):
            resultado = valor1 + valor2
        elif (operacao == 2):
            resultado = valor1 - valor2
        elif (operacao == 3):
            resultado = valor1 * valor2
        elif (operacao == 4 and valor2 != 0):
            resultado = valor1 / valor2
        elif (operacao == 5):
            resultado = valor1 ** valor2
        elif (operacao == 6 and  valor2 != 0):
            resultado = valor1 ** (1/valor2)
        elif (operacao == 7):
            resultado = valor1 *valor2
            valor2 -= 1
            print("\n" + str(resultado) + "x^" + str(valor2) + "\n")
        elif (operacao == 8 and valor2 != -1):
            resultado = valor1 /(valor2 + 1)
            valor2 += 1 
            print("\n" + str(resultado) + str("x^") + str(valor2) + "\n")
        else:
            print("Operacao invalida")

        print(resultado)

    except ValueError:
        print("Valores invalidos")
    except OverflowError:
        print("Estouro de memoria")
    sair = raw_input("Deseja fazer outra operacao? (n para sair)\n")
