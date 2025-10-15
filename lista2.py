"""valores = [] # criando uma lista vazia

for item in range(10,14):
    valores.append(item)

print(valores)    

# Preenchendo uma lista com dados dinâmicos

valores2 = []  # Inicializa a lista vazia

while True:
    num = int(input("Informe um valor numérico qualquer (0 para encerrar): "))
    if num == 0:
        break  # Encerra o sistema
    else:
        valores.append(num)

print("\nValores informados na lista:")
print(valores)"""


#Atividade 

#----------------------------------------------------------------

# Criando uma lista com valores fixos
valores = []
for item in range(10, 14):
    valores.append(item)

print("Lista inicial:", valores)

# Preenchendo uma segunda lista com dados dinâmicos
valores2 = []

while True:
    num = int(input("Informe um valor numérico qualquer (0 para encerrar): "))
    if num == 0:
        break
    else:
        valores2.append(num)

print("\nValores informados na lista dinâmica:")
print(valores2)

# Processo de remoção dos itens da lista principal
# Inicializando a lista com valores fixos
valores = [10, 11, 12, 13]

def mostrar_lista():
    print("\nLista atual:", valores)

while True:
    print("\n--- MENU ---")
    print("1 - Adicionar valor à lista")
    print("2 - Apagar o último valor da lista")
    print("0 - Encerrar o sistema")
    
    opcao = input("Escolha uma opção: ").strip()
    
    if opcao == '1':
        num = int(input("Informe um valor numérico para adicionar: "))
        valores.append(num)
        print(f"Valor {num} adicionado com sucesso!")
        mostrar_lista()
        
    elif opcao == '2':
        if valores:
            removido = valores.pop()
            print(f"Valor {removido} removido da lista.")
        else:
            print("A lista já está vazia.")
        mostrar_lista()
        
    elif opcao == '0':
        print("Encerrando o sistema. Até mais!")
        break
        
    else:
        print("Opção inválida. Tente novamente.")
