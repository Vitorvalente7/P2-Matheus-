#15.comidas = ['leite', 'couve','computador', 'tomate','garfo','faca','tablet','refrigerante']
#bebidas = ['uva', 'colher','TV','vinho','cerveja','celular','banana']
#talheres = ['arroz','iPhone', 'concha','whisky','vodka','feijão','colher de chá']
#criar uma nova lista para eletrônicos e adicionar os eletrônicos a 
#ela e organizar as demais lista

comidas = ['leite', 'couve','computador', 'tomate','garfo','faca','tablet','refrigerante']
bebidas = ['uva', 'colher','TV','vinho','cerveja','celular','banana']
talheres = ['arroz','iPhone', 'concha','whisky','vodka','feijão','colher de chá']
eletrônicos = []

comidas.remove('leite')
comidas.remove('computador')
comidas.remove('garfo')
comidas.remove('faca')
comidas.remove('tablet')
comidas.remove('refrigerante')
comidas.append('uva')
comidas.append('banana')
comidas.append('arroz')
comidas.append('feijão')

bebidas.remove('banana')
bebidas.remove('uva')
bebidas.remove('colher')
bebidas.remove('TV')
bebidas.remove('celular')
bebidas.append('leite')
bebidas.append('refrigerante')
bebidas.append('cerveja')
bebidas.append('whisky')
bebidas.append('vodka')

talheres.remove('arroz')
talheres.remove('iPhone')
talheres.remove('whisky')
talheres.remove('vodka')
talheres.remove('feijão')
talheres.append('garfo')
talheres.append('faca')
talheres.append('colher')

eletrônicos.append('computador')
eletrônicos.append('tablet')
eletrônicos.append('TV')
eletrônicos.append('celular')
eletrônicos.append('iPhone')

print("Lista de comidas atualizada:", comidas)
print("Lista de bebidas atualizada:", bebidas)
print("Lista de talheres atualizada:", talheres)
print("Lista de eletrônicos atualizada:", eletrônicos)