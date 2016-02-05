from Operation import *

def trata_entrada(tipo,texto):
    return tipo(raw_input(texto))

def atribui_valores(operacao):
    operacao.set_operation_type(trata_entrada(int,"Digite 1 para soma, 2 subtracao, 3 multiplicacao, 4 divisao, 5 potencia, 6 raiz, 7 derivada simples, 8 integral simples\n"))
    operacao.set_value1(trata_entrada(float,"Primeiro valor: "))
    operacao.set_value2(trata_entrada(float,"Segundo valor: "))

def seleciona_calculo(operacao):
    operacoes = [operacao.sum_values(), operacao.subtract_values(), operacao.multiply_values(), operacao.divide_values(), 
                 operacao.power_of_value1_by_value2(), operacao.root_of_value1_by_value2(), operacao.derivative_of_value1_by_value2(), 
                 operacao.integral_of_value1_by_value2()]
    operacao.set_result(operacoes[operacao.get_operation_type() - 1])

def executa_operacao(operacao):
    atribui_valores(operacao)
    seleciona_calculo(operacao)
    operacao.adjust_value2()
    print(operacao)

def main():
  sair = ""
  operacao = Operation(0,0,0,0)

  while sair != "n":
      try:
          executa_operacao(operacao)
      except ValueError:
          print("Valores invalidos")
      except OverflowError:
          print("Estouro de memoria")
      except ZeroDivisionError:
          print("Valor 2 resultou em uma divisao em 0, portanto nao sera calculado")
      finally:
          sair = trata_entrada(str,"Deseja fazer outra operacao? (n para sair)\n")

main()
