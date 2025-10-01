# Forma condicional 1 
"""senha = 123 
while senha != 1234:
    senha = int(input("Digite a senha correta:"))
    if senha != 1234:
        print("Senha incorreta, tente novamente.")
print("Obrigado por acessar o sistema!")"""""

# Forma condicional 2

tentativas = 3

while True:
    senha = input("Informe sua senha: ")
    
    if senha == "aluno2":
        print("Senha correta! Acesso liberado.")
        break  # Encerra o loop se a senha estiver correta
    
    tentativas -= 1  # Reduz o número de tentativas
    
    if tentativas <= 0:
        print("Sem tentativas, só lamento.")
        break  # Encerra o loop se não houver mais tentativas
    else:
        print(f"Senha incorreta. Você ainda tem {tentativas} tentativa(s).")


