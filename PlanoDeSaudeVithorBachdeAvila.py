#Sistema de Plano de Saúde
#Trabalho de Vithor Bach de Ávila

#Exibir o nome do desenvolvedor
print("Sistema desenvolvido por Vithor Bach de Ávila")

#Valor base do plano e idade do cliente
valorBase = float(input("Informe o valor do plano: "))
idade = int(input("Informe a idade do cliente: "))

#Calculos para o plano
if idade >= 0 and idade < 19:
    porcentagem = 100 / 100
elif idade >= 19 and idade < 29:
    porcentagem = 150 / 100
elif idade >= 29 and idade < 39:
    porcentagem = 225 / 100
elif idade >= 39 and idade < 49:
    porcentagem = 240 / 100
elif idade >= 49 and idade < 59:
    porcentagem = 350 / 100
elif idade >= 59:
    porcentagem = 600 / 100
else: 
    #Erro de idade e fechar o programa
    print("Idade inválida.")
    exit()

#Calculando o valor mensal
valorMensal = valorBase * porcentagem

#Exibindo o valor calculado
print(f"O valor mensal do plano para sua idade é: R$ {valorMensal: .2f}")
