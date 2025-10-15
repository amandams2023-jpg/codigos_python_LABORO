# Criando uma lista em Python
numeros = [3, 5, 8,10,14]
print(numeros)

#print(type(lista))

numeros[2] = 15

# Exibir todos os números
for item in numeros:
    print(item)

# Inserir um valores na lista
numeros.append(23)

print(numeros)

# Inserir em qlq lugar da lista
numeros.insert(2, 90)  # iremos inserir o valor 90 no índice 2
print(numeros)

# Remover um valor da lista
numeros.pop()#removendo item do final da lista
print(numeros)