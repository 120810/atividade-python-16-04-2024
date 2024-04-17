def montar_menu():
    print("Menu:")
    print("1. Ler vetores A e B")
    print("2. Realizar operações")
    print("3. Sair")

def ler_vetores():
    A = list(map(int, input("Digite os elementos do vetor A separados por espaço: ").split()))
    B = list(map(int, input("Digite os elementos do vetor B separados por espaço: ").split()))
    return A, B

def realizar_operacoes(A, B):
    C = [a * b if a % 2 == 0 else a ** b for a, b in zip(A, B)]
    print("Vetor C resultante:")
    print(C)


A = []
B = []

while True:
    montar_menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        A, B = ler_vetores()
    elif opcao == 2:
        if not A or not B:
            print("Por favor, leia os vetores primeiro.")
        else:
            realizar_operacoes(A, B)
    elif opcao == 3:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
