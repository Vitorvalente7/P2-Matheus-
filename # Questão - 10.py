# Questão - 10
def eh_numero_perfeito(numero):
    soma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            soma_divisores += i
    return soma_divisores == numero
numero = int(input("Digite um número inteiro positivo para verificar se é perfeito: "))
if eh_numero_perfeito(numero):
    print(numero, "é um número perfeito.")
else:
    print(numero, "não é um número perfeito.")
