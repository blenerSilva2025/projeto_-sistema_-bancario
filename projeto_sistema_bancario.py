Menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(Menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    elif opcao == "s":
        saque = float(input("Informe o valor do saque: "))
        if saque > 0 and saque <= limite and numero_saques < LIMITE_SAQUES:
            if saldo >= saque:
                saldo -= saque
                extrato += f"Saque: R$ {saque:.2f}\n"
                numero_saques += 1
                print("Saque realizado com sucesso!")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("Saque inválido ou limite de saques atingido.")

    elif opcao == "e":
        print("\n=== Extrato ===")
        print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("================")

    elif opcao == "q":
        print("Saindo do sistema. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
