from Operation import *

def trataEntrada(tipo,texto):
    return tipo(raw_input(texto))

def atribuiValores(operacao):
    operacao.setOperationType(trataEntrada(int,"Digite 1 para soma, 2 subtracao, 3 multiplicacao, 4 divisao, 5 potencia, 6 raiz, 7 derivada simples, 8 integral simples\n"))
    operacao.setValue1(trataEntrada(float,"Primeiro valor: "))
    operacao.setValue2(trataEntrada(float,"Segundo valor: "))

def selecionaCalculo(operacao):
    if (operacao.getOperationType() == 1):
      operacao.setResult(operacao.sumValues())
    elif (operacao.getOperationType() == 2):
      operacao.setResult(operacao.subtractValues())
    elif (operacao.getOperationType() == 3):
      operacao.setResult(operacao.multiplyValues())
    elif (operacao.getOperationType() == 4):
      operacao.setResult(operacao.divideValues())
    elif (operacao.getOperationType() == 5):
      operacao.setResult(operacao.powerOfValue1byValue2())
    elif (operacao.getOperationType() == 6):
      operacao.setResult(operacao.rootOfValue1byValue2())
    elif (operacao.getOperationType() == 7):
      operacao.setResult(operacao.derivativeOfValue1byValue2())
    elif (operacao.getOperationType() == 8):
      operacao.setResult(operacao.integralOfValue1byValue2()) 

def executaOperacao(operacao):
    atribuiValores(operacao)
    selecionaCalculo(operacao)
    print(operacao)

def main():
  sair = ""
  operacao = Operation(0,0,0,0)

  while sair != "n":
      try:
          executaOperacao(operacao)
      except ValueError:
          print("Valores invalidos")
      except OverflowError:
          print("Estouro de memoria")
      except ZeroDivisionError:
          print("Valor 2 resultou em uma divisao em 0, portanto nao sera calculado")
      finally:
          sair = trataEntrada(str,"Deseja fazer outra operacao? (n para sair)\n")

main()
