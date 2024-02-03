import random

lista_palavras = ['camelo', 'piano', 'viola', 'macaco']
forca = []
TENTATIVAS = 6
jogo_continua = True
tentativas_restantes = TENTATIVAS

palavra_escolhida = random.choice(lista_palavras) #escolhe uma palavra da lista fornecida
print(palavra_escolhida)
palavra_escolhida_lista = list(palavra_escolhida) #transforma a palavra escolhida em uma lista, para ser utilizada no for loop

for char in palavra_escolhida: #cria uma lista em branco
    forca.append("_")
print(f"A palavra é {forca}")
print(f"Você tem {TENTATIVAS} tentativas.")

while jogo_continua == True:
    letra_fornecida = input("Digite uma letra: ")

    for i in range(len(palavra_escolhida_lista)): #for comparando a letra digitada com as letras da palavra
        if palavra_escolhida_lista[i] == letra_fornecida: #Se a letra digitada for igual ao caractere na posição
            forca[i] = letra_fornecida #trocar o caractere na lista em branco pela letra digitada
  
    if letra_fornecida not in palavra_escolhida: #Caso a palavra não possua a letra digitada.
        tentativas_restantes -= 1
        print(f"Está palavra não tem essa letra. Você tem {tentativas_restantes} tentativas.")
    if tentativas_restantes == 0:
        print(f"Você não tem mais tentativas! O jogo acabou. A palavra era {palavra_escolhida}")
        jogo_continua = False
    
    print(forca)
    if forca == palavra_escolhida_lista:
        print(f"Parabéns! Você adivinhou a palavra {palavra_escolhida}.")
        jogo_continua = False