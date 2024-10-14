# OPERADORES RELACIONAIS
# == ingual a 
# != diferente de
# > maior que             membro a esquerda 'operador' membro a direita
# >= maior igual
# < menor que
# <= menor igual

# Desafio da aula do dia 12/10/2024

emprestimo = float(input("quanto de emprestimo voce vai pegar: "))
salario = float(input("valor do seu salario: "))

if (emprestimo <= 0.5 * salario ):
    print ("emprestimo aprovado")
    
elif (emprestimo <= 0.75 * salario):
    print ("vamos analisar")    
    
else:
    print ("emprestimo negado")



cupoom = input("Voce tem o cupom: " )
#  nao pode usar o and 
if (cupoom == 'FUCTURA1' or cupoom == 'FUCTURA2'):
    print('Aplicar o desconto de 15%')

else:
    print('nao fazer nada')   
    
cupomzinho = input("digite o nome do seu cupom ai cmpç: ")   

if (cupomzinho == "FUCTURA1"):
    print("desconto de 15%")
    
elif (cupomzinho == "FUCTURA2"):
    print("desconto de 10%")

else:
    print("desconto de 5%")
    
    
 
 
 
#  Um cliente solicita um cartão de crédito ao banco. Se a renda mensal for maior ou igual a R$ 5.000, o 
#  banco concede um cartão com limite de R$ 10.000. Se a renda for maior ou igual a R$ 3.000 e menor que R$ 5.000,
#  o banco concede um cartão com limite de R$ 5.000. Se a renda for menor que R$ 3.000, o banco nega o cartão de crédito.
#  (ações: 1 – conceder cartão com limite de R$ 10.000, 2 – conceder cartão com limite de R$ 5.000, 3 – negar o cartão). 

minharenda = float(input("Qual sua renda mensal: "))

if (minharenda >= 5000):
    print("Vc vai ter um limite de R$ 10.000 ")
    
elif (minharenda >= 3000 and  minharenda < 5000): 
    print("Vc vai ter um limite de R$5.000")   
          
else:
    print("cartão negado")       
    
# Um cliente solicita um financiamento para a compra de uma casa. Se o valor solicitado for menor ou igual
# a 40% do valor total do imóvel, o financiamento será aprovado. Se o valor for entre 40% e 70%,
# a situação ficará em análise. Se o valor for maior que 70% do valor do imóvel, 
# o financiamento será negado. (ações: 1 – aprovar o financiamento, 2 – situação em análise, 3 – negar o financiamento).

valor = float(input("qual o valor vc deseja: "))    
valordoimovel = 10000

if (valor <= 0.4 * valordoimovel):
    print("aprovado")
    
elif (0.4 * valordoimovel < valor <= 0.7 * valordoimovel):    
    print("analise")

elif (valor > 0.7* valordoimovel):
    print("negado")
    
    