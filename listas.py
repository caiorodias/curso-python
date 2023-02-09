# Métodos para List


## Append = adiciona
lista = []

lista.append(1)
lista.append('Python')
lista.append([40, 30, 20])

print(lista)

## Clear = limpa

lista.clear()

print(lista)

## Count = dizer quantas vezes algum objeto aparece na sua lista

cores = ['vermelho', 'azul', 'verde', 'azul']

print(cores.count('vermelho'))
print(cores.count('azul'))
print(cores.count('verde'))

## Extend = juntar listas
### Não elimina valores duplicados

linguagens = ['python', 'js', 'c'] 

print(linguagens)

linguagens.extend(['java', 'C#'])

print(linguagens)

# Index = qual a posição da primeira aparição de algum objeto na lista

print(linguagens.index('java'))
print(linguagens.index('python'))

# Pop = retira o último item adicionado

print(linguagens.pop()) #retirou o C#
print(linguagens)

# Remove = Remove o item, pelo seu nome
## Retira apenas a primeira aparição do item

linguagens.remove('c')
print(linguagens)

# Reverse = Espelhar a lista

linguagens.reverse()
print(linguagens)

# Sort = Deixa a lista em ordem alfabética

linguagens = ['python', 'js', 'c', 'java', 'c#']
linguagens.sort()
print(linguagens)

## ordem alfabética ao contrário

linguagens.sort(reverse=True)
print(linguagens)

## ordenar pelo tamanho das palavras, crescente

linguagens.sort(key=lambda x: len(x))
print(linguagens)

## ordenar pelo tamanho das palavras, decrescente

linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)

# Len = diz o tamanho da lista / item

print(len(linguagens))

# Sorted = mesma função que a sort

print(sorted(linguagens, key=lambda x: len(x)))

print(sorted(linguagens, key=lambda x: len(x), reverse=True))
