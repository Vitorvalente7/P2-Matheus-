lista = []

while True:
    elemento = input("Digite um elemento para adicionar à lista (ou 'parar' para encerrar): ")
    if elemento == 'parar':
        break
    lista.append(elemento) 

print("Lista completa:")
print(lista)

