soma = 0
contador = 0 
while True:
    numero = int(input("Digite um número inteiro (digite 0 para parar): "))
    if numero == 0:
        break
    soma += numero  
    contador += 1  
if contador > 0:
    print("A soma dos {} números digitados é: {}".format(contador, soma))
else:
    print("Nenhum número foi digitado para somar.")
