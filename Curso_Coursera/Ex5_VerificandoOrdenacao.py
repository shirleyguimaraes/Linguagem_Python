
def main():

    n1 = int(input("Digite um número inteiro: "))
    n2 = int(input("Digite outro número inteiro: "))
    n3 = int(input("Digite mais número inteiro: "))

    if n1 < n2 < n3 :
        print("Crescente")
    else:
        print("Não está na ordem crescente.")

main()