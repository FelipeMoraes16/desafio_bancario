menu = """
=====Menu=====

[0] Depositar
[1] Sacar
[2] Extrato
[3] Novo Usuário
[4] Nova Conta
[5] Sair

=====Menu=====
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3
usuarios = []
contas = []
AGENCIA = "0001"
    
def deposito(deposito_saldo, deposito_extrato, /):
    print("=====Deposito=====")
    
    deposito = float(input("Digite o valor a ser depositado: "))

    if deposito > 0:
        deposito_extrato += f"Deposito R$ {deposito:0.2f}\n"
        deposito_saldo += deposito
        print("=====Deposito=====")

    else:
         print("Operação falhou, digite um valor acima de R$ 1,00")
         print("=====Deposito=====")

    return deposito_saldo, deposito_extrato

def saque(*, saque_saldo, saque_extrato, saque_numero):
    print("=====Saque=====")
    
    if saque_numero < LIMITE_SAQUE:
        valor_saque = float(input("Digite o valor de saque: "))

        if valor_saque < saque_saldo:

            if valor_saque <= 500:

                if valor_saque > 0:      
                    saque_extrato += f"Saque -R${valor_saque:0.2f}\n"
                    saque_saldo -= valor_saque
                    saque_numero += 1
                    print("=====Saque=====")
                
                else:
                    print("Digite um valor acima de R$ 1,00")
                    print("=====Saque=====")

            else:
                print("Operação falhou, valor de saque excedido")
                print("=====Saque=====")

        else:
            print("Operação falhou, saldo insuficiente")
            print("=====Saque=====")  

    else:
        print("Operação falhou, limite de saque diario excedido")
        print("=====Saque=====")
    
    return saque_saldo, saque_extrato, saque_numero

def funcao_extrato(extrato_final, /, *, extrato_saldo):

    ter_algo_extrato = extrato_final != ""

    if ter_algo_extrato:
        print("=====Extrato=====")
        print(f"{extrato_final}")
        print(f"Saldo: R$ {extrato_saldo:0.2f}")
        print("=====Extrato=====")

    else:
        print("=====Extrato=====")
        print("Não houve nenhuma movimentação na conta\n\n")
        print(f"Saldo: R$ {extrato_saldo:0.2f}")
        print("=====Extrato=====")

    return extrato_final, extrato_saldo

def criar_usuarios(usuarios):
    print("=====Novo Usuário====")
    cpf = input("Informe o CPF (somente os numeros): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\nJá existe um usuario com esse CPF!")
        print("=====Novo Usuário====")
        return
    
    nome = input("Informe o nome complete: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso !")
    print("=====Novo Usuário====")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    print("=====Criar Conta=====")

    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("=====Conta criada com sucesso!=====")
        print("=====Criar Conta====")
        return{"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    
    print("Usuário não encontrado")
    print("=====Criar Conta=====")

while True:

    opcao = input(menu)

    if opcao == "0":
        saldo, extrato = deposito(saldo, extrato)
    
    elif opcao == "1":
        saldo, extrato, numero_saques = saque(saque_saldo = saldo, saque_extrato = extrato, saque_numero = numero_saques)
    
    elif opcao == "2":
        funcao_extrato(extrato, extrato_saldo = saldo)

    elif opcao == "3":
        criar_usuarios(usuarios)

    elif opcao == "4":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)

    elif opcao == "5":
        break

    else:
        print("=====Menu=====")
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        print("=====Menu=====")

    