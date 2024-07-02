# Questao 6
entrada = input("Digite a lista de números separados por espaço: ")
numeros_str = entrada.split()
numeros = list(map(int, numeros_str))
num_max = max(numeros)
num_min = min(numeros)
print(f"O maior número da lista é: {num_max}")
print(f"O menor número da lista é: {num_min}\n")
print("Lista original de números (em formato de string):", numeros_str)
