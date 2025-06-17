print('------------------------------------')
#usar a função dict
person2 = dict(nome = 'Maria', sexo = 'Feminino', idade = 28, casado = True)

print(person2)
print(type(person2))

print('------------------------------------')
#outra forma de função dict

print(person2['sexo'])
print(person2['idade'])

print('------------------------------------')
#criar dict vazio e adicionar coisas nele

dict1 = {}
print(dict1)
dict1['Chave'] = 'nao esta mais vazio!'
print(dict1)

print('------------------------------------')
#

dict2 ={'Pessoa1':['willian',30,'professor'],
        'Pessoa2':['Danilo',16,'aluno']}
print(dict2)
print(dict2['Pessoa2'])

print('------------------------------------')
#dicionário alinhado

pessoa = {
    'nome': 'Joao',
    'idade': 30,
    'endereço':{
        'rua': 'Rua Principal',
        'cidade': 'cidade A',
        'estado': 'estado X'
    }
}

print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['endereço'])
print(pessoa['endereço']['rua'])

print('------------------------------------')
#adicionando valores no dicionário 

print('Nome:',pessoa['nome'])
print('Idade:',pessoa['idade'])
print('Endereco:',pessoa['endereço'])

print('------------------------------------')
#usar o método get, busca na chave

print(person2.get('nome'))

print('------------------------------------')
#alterar a informação já criada

person2['casado'] = True
#adicionar um novo campo e chave
person2['Nacionalidade'] = 'Brasileiro'

print(person2)

print('------------------------------------')
#mostrar todas as chaves do dicionário

print(person2.keys())
print(person2.values())

print('------------------------------------')

# criando um dicionário
meudicionario = {'a': 1, 'b': 2, 'c': 3}

# exibindo o dicionário original
print('Dicionario original:', meudicionario)

# usando o clear para remover todos os itens
meudicionario.clear()

# exibindo o dicionário após o clear
print('Dicionario apos o clear:', meudicionario)

print('------------------------------------')

# verificação antes de tentar deletar a chave 'b'
if 'b' in meudicionario:
    del meudicionario['b']
    print('Dicionario apos deletar b:', meudicionario)
else:
    print("A chave 'b' não existe no dicionário, portanto não pode ser deletada.")

# limpando novamente (embora já esteja vazio)
meudicionario.clear()
print('Dicionario apos o clear:', meudicionario)

print('------------------------------------')

# dicionario original
dicionario1 = {'a': 1, 'b': 2}

# adicionando elementos de outro dicionario
dicionario2 = {'b': 3, 'c': 4}
dicionario1.update(dicionario2)

# exibindo o dicionario apos a atualização
print('Dicionario apos o update:', dicionario1)

print('------------------------------------')

# Criando um dicionário de estoque e atualizando os valores
estoque = {'macas': 10, 'banana': 15, 'laranjas': 8}
print("Estoque: ", estoque)
# Atualizando os valores
estoque['macas'] = 5
print("Estoque atualizado:", estoque)

print('------------------------------------')
#aula_05 se inicia aqui

#criação
frutas = ('banana','uva','laranja')
print(frutas)
print(type(frutas))

#verificar o tamanho
len(frutas)

#pegar o primeiro e ultilmo item
print(frutas[0])
print(frutas[-1])

#não sei uma legenda, estou com muitoo sonooo
tupla_del = ('a',1,3,5,'d')

print('------------------------------------')

minha_lista = [4, 5, 6]
tupla_resultante = tuple()
print(tupla_resultante)

print('------------------------------------')

#escreva um programa python que crie uma tupla fruta = ('maca','abacaxi','caju') insira o item 'tomate' sem apagar a tupla

#tupla original
fruta = ('maca', 'abacaxi', 'caju')
print('Tupla original:', fruta)

#adicionar o tomate
nova_fruta = fruta + ('tomate',) #a virgula, o python reconhece como tupla de um item, se não houver, ele reconhece com string

#resultado
print('Atualizacao: ', nova_fruta)
