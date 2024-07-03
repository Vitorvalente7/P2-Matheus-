# Questão - 4
def remover_duplicatas(lista):
    lista_sem_duplicatas = []
    for elemento in lista:
        if elemento not in lista_sem_duplicatas:
            lista_sem_duplicatas.append(elemento)
    return lista_sem_duplicatas
minha_lista = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9]
lista_sem_duplicatas = remover_duplicatas(minha_lista)
print("Lista sem duplicatas:", lista_sem_duplicatas)
