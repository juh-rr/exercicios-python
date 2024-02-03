# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def reverso (num):
    numstr = str(num)
    lista_num = []
    for char in numstr:
        lista_num.append(char)
    lista_num.reverse() #reverter a ordem dois valores da lista
    novo_num = "".join(lista_num) #juntar os elementos da lista em um único str
    print(novo_num)


numero = int(input("Digite um número: "))
reverso(numero)


