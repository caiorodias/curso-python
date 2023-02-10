# É uma lista que elimina itens repetidos

print(set([1, 2, 3, 1, 3, 4]))

#{1, 2, 3, 4}

print(set('abacaxi'))

#{'b', 'x', 'a', 'c', 'i'}

# Também da pra criar um conjunto com {}

linguagens = {'pyton', 'java', 'python'}
print(linguagens)

# Conjuntos em Python não suportam indexação ou fatiamento. Para acessar é necessário converter para uma lista

numeros = {1, 2, 3, 2}

numeros = list(numeros)

print(numeros[0])

# Porém é possivel percorrer um set

carros = {'gol', 'celta', 'palio', 'celta'}

for carro in carros:
    print(carro)
    
    
for indice, carro in enumerate(carros):
    print(f'{indice}: {carro}')
    
    
# Métodos Union = uniao de 2 conjuntos

conjunto_a = {1, 2}
conjunto_b = {3, 4}

print(conjunto_a.union(conjunto_b))

# Intersection = interseção dos conjuntos

conjunto_c = {1, 2, 3}
conjunto_d = {2, 3, 4}

print(conjunto_c.intersection(conjunto_d))

# Difference = Diz o que tem em um conjunto X que não tem no conjunto Y

conjunto_c = {1, 2, 3}
conjunto_d = {2, 3, 4}

print(conjunto_c.difference(conjunto_d))
print(conjunto_d.difference(conjunto_c))

# Symmetric_difference = É o contrario da intersection, diz os itens que estão diferente nos conjuntos

conjunto_c = {1, 2, 3}
conjunto_d = {2, 3, 4}

print(conjunto_c.symmetric_difference(conjunto_d))

# Issubset = Diz se conjunto A pertence a Be retorna True ou False

conjunto_e = {1, 2, 3}
conjunto_f = {4, 1, 2, 5, 6, 3}

print(conjunto_e.issubset(conjunto_f)) # O conjunto E pertence ao conjunto F?
print(conjunto_f.issubset(conjunto_e)) # O conjunto F pertence ao conjunto E?

# Issuperset = Contrário. A tem todos de B?

conjunto_e = {1, 2, 3}
conjunto_f = {4, 1, 2, 5, 6, 3}

print(conjunto_e.issuperset(conjunto_f)) # O conjunto E tem todos do conj F?
print(conjunto_f.issuperset(conjunto_e)) # O conjunto F tem todos do conj E?

# Isdisjoint = Conjuntos disjuntos. O conjunto x é totalmente diferente de Y? True ou False?

conjunto_g = {1, 2, 3, 4, 5}
conjunto_h = {6, 7, 8, 9}
conjunto_i = {1, 0}

print(conjunto_g.isdisjoint(conjunto_h)) #True
print(conjunto_g.isdisjoint(conjunto_i)) #False

# Add = adiciona um elemento, se ele já não existir no conjunto

sorteio = {1, 23}

sorteio.add(25)
sorteio.add(42)
sorteio.add(25)

print(sorteio)

# Clear = limpar todo o conjunto

# Copy = copiar o conjunto

# Discard = retira um valor do conjunto, se for passado um valor que não existe no conjunto, simplesmente ele ignora

numeros = {1, 2, 3, 4, 5}

numeros.discard(1)

print(numeros)

numeros.discard(18)

print(numeros)

# Pop = retira sempre o primeiro numero do conjunto

numeros = {1, 2, 3, 4, 5}

numeros.pop()

print(numeros)

numeros.pop()

print(numeros)

# Remove = igual o discard, porém se o elemento não existe ele dá um erro


# Len = retorna a quantidade de itens no conjunto

# In = verifica se um item está em um conjunto

numeros = {1, 2, 3, 4, 5}

print(4 in numeros)
print(9 in numeros)