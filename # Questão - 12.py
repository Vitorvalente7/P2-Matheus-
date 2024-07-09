# Questão - 12
nacionalidade = input("Digite a sua nacionalidade: ")
anos_de_experiencia = float(input("Digite os anos de experiencia: "))
if idade >= 18 and anos_de_experiencia >= 2:
    if nacionalidade == "Brasileiro" or nacionalidade == "Brasileira":
        print("Você se encaixa nos critérios para vaga de emprego!")
    else:
        print("Você não se encaixa nos critérios para vaga de emprego!")
else:
    print("Você não está apto à vaga de emprego!")

