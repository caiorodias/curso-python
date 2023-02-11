# Chave: valor

## Formas de declarar dicionario

pessoa = {'nome': 'Guilherme', 'idade': 28}

print(pessoa)

pessoa2 = dict(nome = 'Guilherme', idade = 28)

print(pessoa2)

## Para adicionar novas chaves

pessoa['telefone'] = '3333-1234'

print(pessoa)

## O dicionario não adiciona novos valores a uma chave, ele substitui os valores

pessoa['nome'] = 'Maria'

print(pessoa)

# Métodos Dict

# Clear = limpa

# Copy = copia

contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'}
}

print(contatos)

copia = contatos.copy()
print(copia)

copia['guilherme@gmail.com'] = {'nome': 'Gui'}
print(copia)

# Fromkeys = Quando você quer adicionar chaves com valor vazio/none ou padrão

print(dict.fromkeys(['nome', 'telefone']))

print(dict.fromkeys(['nome', 'telefone'], 'vazio'))

# Get = Retorna o valor de uma chave, se a chave não existir, por padrão retorna None, mas pode ser inserido um retorno padrão para se ela não existir

contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'}
}

print(contatos.get('chave')) #None

print(contatos.get('chave', {})) # Se a chave 'chave', não existir, retorte {}

print(contatos.get('guilherme@gmail.com', {})) # Se a chave guilherme@gmail.com não existir retorne {}

# Items = retorna tuplas

contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'}
}

print(contatos.items())

# Keys = Retorna só as chaves do dict

contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'}
}

print(contatos.keys())

# Pop = Remove uma chave e retorna o valor que ele removeu e se não existir pode passar um valor padrao para retornar

contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'}
}

print(contatos.pop('guilherme@gmail.com'))

print(contatos.pop('guilherme@gmail.com', 'não encontrou')) # Se não colocar um valor padrão e ela não existir vai dar erro

# Popitem = a diferença é que não informamos as chaves e ele vai retirando os itens na sequencia

# Setdefault = Se o atributo já existir no dict ele não muda, mas se não existir ele acrescenta com o valor padrão inserido

contato = {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault('nome', 'Giovanna') # Se não existir a chave/ valor Nome:Giovana, ele acrescenta, se não, não muda
print(contato)

contato.setdefault('idade', 28) # Se o chave/valor não existir ele cria
print(contato)

# Update = atualiza o dict

contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'}
}

contatos.update({'caio@gmail.com': {'nome': 'Caio', 'telefone': '3311-3333'}})

print(contatos)

print(contatos.keys())

# Values = Ao contrário do Keys, ele retorna todos os valores dos dicts

# In = Verifica se aquilo está dentro do dict e retorna True ou False

contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'},
    'caio@gmail.com': {'nome': 'Caio', 'telefone': '3333-2222'},
    'glennda@gmail.com': {'nome': 'Glennda', 'telefone': '3333-2223'},
    'ana@gmail.com': {'nome': 'Ana', 'telefone': '3333-2224'},
}

print('caio@gmail.com' in contatos) # Existe essa chave?
print('flavia@gmail.com' in contatos)
print('idade' in contatos['glennda@gmail.com'])
print('telefone' in contatos['ana@gmail.com']) # Buscando dentro de uma key

# Del = deleta o objeto que você quer

contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'},
    'caio@gmail.com': {'nome': 'Caio', 'telefone': '3333-2222'},
    'glennda@gmail.com': {'nome': 'Glennda', 'telefone': '3333-2223'},
    'ana@gmail.com': {'nome': 'Ana', 'telefone': '3333-2224'},
}

del contatos['glennda@gmail.com']['telefone'] # Deletar o telefone de Glennda
del contatos['guilherme@gmail.com'] # Deletar a chave completa de Guilherme

print(contatos)