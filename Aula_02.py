#declarar uma string
dia_da_semana = "segunda"
mes = "janeiro"

print(dia_da_semana)
print(mes)

print("------------------------")

#usando a função len
print(len(dia_da_semana))
print(len(mes))

print("------------------------")

#primeira letra da string
print(dia_da_semana[0])

#ultima letra da string
print(dia_da_semana[-1])

#pedaço do texto
print(dia_da_semana[0:4])

print("-----------------------")

#deixar em minusculo
print(dia_da_semana.lower())

#deixar em maiusculo
print(dia_da_semana.upper())

#deixar só a primeira letra em maiusculo
print(dia_da_semana.capitalize())

#permitir que esses meteodos se alternam
print(dia_da_semana) #seria necessario mais palavras nessa variável

print("-----------------------")

nome = 'Danilo e um '
frase = nome + 'desenvolvedor j. 1'

print(frase.replace('j.','pleno'))

print("-----------------------")

nome = 'Danilo e um '
frase = nome + 'desenvolvedor pleno 1'

print(frase.replace('1','3').replace('Danilo','Gabriel'))

print("-----------------------")

nome = 'julia tem acento!'

print(nome.replace('julia','O nome julia').upper())

print("-----------------------")

#mudar tudo para minusculo e também logo depois do @
email = 'Joana.Silva@EMPRESAANTIGA.com'

print(email.lower().replace('empresaantiga','empresanova'))

print("-----------------------")
#contar o numero de letras (como posso melhorar?)

print(frase)
print(frase.count('a'))

print("-----------------------")

#quebrar texto
print(frase)
print(type(frase))
frase_split =  frase.split(' ')
print(frase_split)
print(type(frase_split))

print("-----------------------")

#quebrar espaços
frase1 = '       bom_dia      '
frase1_split = frase1.split()
print(frase1)
print('Correcao:')
frase_split =  frase1.split(' ')
print(frase1_split)
print(type(frase1_split))

print("-----------------------")

print("Conta-me qualquer coisa...")
anything = input #aqui você muda colocando "()" parenteses, pois no VS Code e alguns lugares não é possível rodar
print("Hum...", anything, "... Realmente?")

print("-----------------------")

print('O texto comeca na primeira linha \n combina na segunda linha')

print('\n')
print('\n')
print('\n')

print('pulei tres linhas')

print("-----------------------")

#tipos de print:
nome ='Danilo'
idade = 16
print('Ola, ' + nome + '! Voce tem ' + str(idade) + ' anos.')

#meteodo antigo - mesma coisa, mas de forma 'ágil'
nome = 'Danilo'
idade = 16
print('Ola, %s! Voce tem %d anos.' % (nome,idade))

print("-----------------------")

print("Fim da Aula")