""" Exercício 2.1 """
''' Tentativa 0 - Dados dois inteiros a e b, calcular a sua soma. '''
''' def main ():
    a = 3
    b = 4
    soma = a+b
    print("A soma de a + b é igual a soma")

main()

print()
soma1 = 9999
print("Olá, mundo!")
print("A soma é", soma1)
print()
print()
'''

'''Tentativa 1'''
'''
n1 = int(input("Dígite um número"))
n2 = int(input("Digite outro número"))
soma2 = n1+ n2
print("A soma de", n1, "mais", n2, "é", soma2)
'''

'''Tentativa 2'''
'''def main ():
    a = 3
    b=4
    soma=a+b
    print("A soma de", a, "+", b, "é igual a", soma)

main()
'''

'''Tentativa 3'''
'''
def main():
    a = input("Digite o primeiro número: ")
    b = input("Digite o segundo número: ")
    soma = a+ b
    print("A soma de", a, "+", "é igual a", soma)

main()
'''
'''Tentativa 4'''
'''
def main():
    a_str = input("Digite o primeiro número:") #Guarda srtings
    b_str = input("Digite o segundo número:") #Guarda strings

    a_int = int(a_str) #converte string/texto para números inteiro
    b_int = int(b_str) #converte string/texto para números inteiro

    soma = a_int +b_int #calcula a soma entre valores que são números inteiros

    print("A soma de", a_int, "+", b_int, "é igual a", soma)

main()
'''

'''Tentativa 5'''
'''
def main():
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    soma = a + b
    print("A soma de", a, "+", b, "é igual a", soma)

main()
'''

'''Exercício 2.2'''
'''Tentativa 0'''
'''Dada a sequência de números inteiros diferentes de zero, terminada por um zero, calcular a sua soma. 
Sequência: 12 17 4 -6 8 0 '''
'''
def main ():
    num = int(input("Digite um inteiro: "))
    soma = 0

    while num != 0:
        soma = soma + num
        num = int(input("Digite um inteiro: "))

    print("A soma é", soma)

#------------------------------------------
main()
'''

'''Exercício 2.3'''
'''Tentativa 0'''
'''Dados números inteiros n e k com k>=0 , calcular n elevado a k. Ex: Dados os números 3 e 4 o seu programa
 deve escrever o número 81'''
'''
def main():
    n = int(input("Digite o valor de n: "))
    k= int(input("Digite o valor de k: "))

    pot = 1
    i= 0
    while i < k:
        pot = pot * n
        i   = i + 1
    print("A potência é", pot) #print mais simples
    print("O valor de %d elevado a %d é %d" %(n,k, pot))

#-------------------------------------
main()
'''

'''Exercício 2.4'''
'''Dado um número inteiro n>= 0, calcular n!.'''

'''
def main():
    n = int(input("Digite o valor de n: "))
    fat = 1
    i = 2
    while i <= n:
        fat = fat * i
        i = i + 1

    print("O valor de %d! é = " % n, fat)


# -----------------------------------------
main()
'''

"""Faz um exemplo do exercíco 2.4 usando a fórmula do n!"""
