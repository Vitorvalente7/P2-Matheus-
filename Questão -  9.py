#9. Criação de uma Calculadora: Escreva um programa que 
#implemente uma calculadora simples que pode realizar quatro 
#operações básicas: soma, subtração, multiplicação e divisão.

num1=float(input("Digte um número: "))
num2=float(input("Digite um número: "))
operação=input("Digite o sinal da operação: ")
if operação == '+':
    print(num1 + num2)
elif operação == '-':
    print(num1 - num2)
elif operação == '*':
    print(num1 * num2)
elif operação == '/':
    print(num1 / num2)
else:
    print("Erro!")