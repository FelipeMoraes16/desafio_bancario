menu = """
=====Menu=====

[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair

=====Menu=====
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "0":
        print("=====Deposito=====")
        deposito = float(input("Digite o valor a ser depositado: "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Deposito: R$ {deposito:0.2f}\n"
            print("=====Deposito=====")

        else:
            print("Operação falhou, digite uma valor acima de R$ 1,00")
            print("=====Deposito=====")

    elif opcao == "1":
        print("=====Saque=====")
        if numero_saques < LIMITE_SAQUE:
            valor_saque = float(input("Digite o valor para saque: "))

            if valor_saque <= limite:

                if valor_saque <= saldo:

                    if valor_saque > 0:
                        saldo -= valor_saque
                        extrato += f"Saque: -R$ {valor_saque:0.2f}\n"
                        numero_saques += 1
                        print("=====Saque=====")

                    else:
                        print("Operação falhou, digite uma valor acima de R$ 1,00")
                        print("=====Saque=====")

                else:
                    print("Operação falhou, saldo insuficiente")
                    print("=====Saque=====")

            else:
                print("Operação falhou, valor de saque excedido")
                print("=====Saque=====")

        else:
            print("Operação falhou, limite de saque diario excedido")
            print("=====Saque=====")
    
    elif opcao == "2":
        print("=====Extrato=====")
        if extrato != "":
            print(f"{extrato}\n")
            print(f"Saldo: R$ {saldo:0.2f}")
            print("=====Extrato=====")
        else:
            print("Não houve nenhuma movimentação na conta\n\n")
            print(f"Saldo: R$ {saldo:0.2f}\n")
            print("=====Extrato=====")
    
    elif opcao == "3":
        break

    else:
        print("=====Menu=====")
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        print("=====Menu=====")

    