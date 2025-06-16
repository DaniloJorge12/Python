#Continuação dos tipos de Print - Dica, não confunda () com {}

#meteodo format()

nome = 'Danilo'
idade = 16
print("Ola, {}! Voce tem {} anos.".format(nome, idade))

#meteodo f (Format Strings)

nome = 'Danilo'
idade = 16
print(f"Ola, {nome}! Voce tem {idade} anos.")

print('-------------------------')

#Print e Input

nome = input #aqui você muda colocando "()" parenteses, pois no VS Code e alguns lugares não é possível rodar
print("Ola, nome !Bem vindo.")#aqui você muda colocando "()" parenteses, pois no VS Code e alguns lugares não é possível rodar

print('-------------------------')

user = input #aqui você muda colocando "()" parenteses, pois no VS Code e alguns lugares não é possível rodar
#frase = user[-1]
print('frase')

print('-------------------------')

primeiroNome = input #aqui você muda colocando "()" parenteses, pois no VS Code e alguns lugares não é possível rodar
segundoNome = input #aqui você muda colocando "()" parenteses, pois no VS Code e alguns lugares não é possível rodar
terceiroNome = input #aqui você muda colocando "()" parenteses, pois no VS Code e alguns lugares não é possível rodar
print(f'EAE {primeiroNome} {segundoNome} {terceiroNome}, Seja Bem-Vindo Mannnn! ') #aqui você muda colocando "()" parenteses, pois no VS Code e alguns lugares não é possível rodar

print('-------------------------')

frase = 'Eu gosto de programar Java'
Nova_palavra = 'Python'
Antiga_palavra = 'Java'

print(frase)

final = (frase.replace('Java','Python'))
print(final)

print('-------------------------')

#no caso deste exemplo, e impossivel prosseguir no vs code usando o input ativado
A = 'Diga-me outro número ' #input('texto')
B = 'Diga-me outro número ' #input('texto')
print('A soma e ') # A + B

print('-------------------------')

#declarar uma lista
frutas = ['banana','uva','manga']

print (frutas)
print (type(frutas))

print('-------------------------')

#pegar os itens da lista por posição
print('|' + frutas[0] + '|')
print('|' + '------|')
print('|' + frutas[1] + '   |')

print('-------------------------')

#declarar outros tipos na lista
a_lista = ['banana',None,'uva','goiaba',4==4]

print(a_lista)

print('-------------------------')

#colocando uma lista em uma lista
a_list = [23,None, 3.14, frutas, 3 <= 5]

print(a_list)

print('-------------------------')

print(a_list[0])

print('-------------------------')

print(a_list[3][1])

print('-------------------------')

#criando uma matrix 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz)
print(type(matriz))

print('-------------------------')

print(matriz[0][0])

print('-------------------------')

#modificando elementos da matriz
matriz[0][0] = 10
matriz[1][2] = 'a'

print(matriz)

#declarar lista vazio
lista_vazia = []
print(lista_vazia)

print('-------------------------')

#utilizar o len

print('|',len(lista_vazia) , '|')
print('|','--|')
print('|',len(frutas) , '|')

print('-------------------------')

#pegar pedaço da lista
print(a_lista)
print('\n')
print(a_lista[2:4])

print('-------------------------')

#um valor tambem pode ser inserido
frutas.insert(1, 'melao')

print(frutas)

print('-------------------------')

#existe o append tambem para inserir
frutas.append('maca')

print(frutas)

#lista de frutas adicionais
frutas_adicionais = ['Caju','morango','abacaxi']

#entendendo a lista de frutas com a listas de frutas de frutas adicionais
frutas.extend(frutas_adicionais)

print(frutas)

print('-------------------------')

#criando lista
numbers = [1,2,3,4,3,5]
#removendo o numero 3 da lista
numbers.remove(3)
#para remover o outro numero 3 é necessário replicar a linha anterior 
print(numbers)

print('-------------------------')

#pop permite pegar o valor que você removeu e passar para uma variável
print(frutas)
fruta_removida = frutas.pop(2)
print(frutas)
print(fruta_removida)