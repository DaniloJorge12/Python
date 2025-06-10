print("O NUMERO E PAR SE FOR 0: " , 10%2) #verifica se é par ou impar (0 ou 1)
print("-----------------------------")

y = 10 #variável
print(y)
print(type(y)) #Tipo do que é mostrado

z = "hello, " , y
print(y)

print("------------------------------")

cidade1, cidade2, cidade3 = 'sao_paulo', 'rio_de_janeiro', 'belo_horizonte' #tudo em uma única linha, mais de uma variável 

print(cidade1)
print(cidade2)
print(cidade3)

print("-----------------------------")

velocidade, resultado, distancia = 10, 32, 87 #novamente, calcula tudo de várias variáveis em uma só
total = velocidade + (4 * resultado) - distancia 

print("O total disso e: " , total)

print("-----------------------------")

primeiroNome = "Danilo"
segundoNome = "Valle M."
terceiroNome = "Jorge"

nomeCompleto = primeiroNome + ' ' + segundoNome + ' ' + terceiroNome #utilizar +, e não virgula.

print(nomeCompleto)

print("---------------------------")

a = 10
b = 20
soma = a + b
print(soma)

print("---------------------------")

celsius = 30
fahrenheit = (celsius * 9/5) + 32
print(fahrenheit)

print("--------------------------")

salario = 3000
INSS = 8/100 * salario
liquido = salario - INSS
print("O salario bruto e " + str(salario) + ", o INSS do salario e " + str(INSS) + ", e por fim, o salario líquido e " + str(liquido))
