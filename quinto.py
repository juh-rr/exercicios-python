'''Crie uma função chamada contar_vogais que recebe uma string como parâmetro. 
Implemente a lógica para contar o número de vogais na string e retorne o total de vogais. 
Solicite a o usuário para inserir uma frase e utilize a função para contar as vogais.'''

def contar_vogais(frase):
    contador_vogal = 0
    for char in frase:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            contador_vogal += 1
    print(f"Essa frase possui {contador_vogal} vogais.")

texto = input("Digite uma frase e irei contar quantas vogais ela tem: ")
contar_vogais(texto)
