#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def somatres (n1, n2, n3):
    soma = n1 + n2 + n3
    frase = print(f"A soma dos três números é {soma}.")
    return frase

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

somatres(num1, num2, num3)