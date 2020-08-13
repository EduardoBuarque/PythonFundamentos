# coding:  iso-8859-1
# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que voc� aprendeu nos cap�tulos 2 e 3. 
# A solu��o ser� apresentada no pr�ximo cap�tulo!
# Assista o v�deo com a execu��o do programa!

SOMA = 1
SUB = 2
MULTI = 3
DIV = 4
operaca_escolhida = ""

print("\n******************* Python Calculator *******************")
print("Selecione uma das operações:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
operacao = int(input("Digite sua opção (1/2/3/4): "))

if operacao in (SOMA, SUB, MULTI, DIV):
    resultado = 0
    numero1 = int(input("Digite o primeiro numero: "))
    numero2 = int(input("Digite o segundo numero: "))
    if operacao == SOMA:
        operaca_escolhida = 'Soma'
        resultado = (numero1 + numero2)
    elif operacao == SUB:
        operaca_escolhida = 'Subtração'
        resultado = numero1 - numero2
    elif operacao == MULTI:
        operaca_escolhida = 'Multiplicação'
        resultado = numero1 * numero2
    elif operacao == DIV:
        operaca_escolhida = 'Divisão'
        resultado = numero1 / numero2
print("O Resultado da {0}: {1}".format(operaca_escolhida, resultado) )