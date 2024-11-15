menu ='''
=========================
[d] = Depositar
[s] = Sacar
[e] = Extrato
[q] = Sair
=========================

=>'''

saldo = 0
numero_saque = 0
LIMITE_SAQUE = 3
limite = 500
extrato = ""

while (True):
    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Digite o valor do depósito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"Realizado o depósito no valor de R$ {valor_deposito:.2f}\n")
        else:
            print("Operação falhou!!! Valor inválido")

    elif opcao == "s":
        valor_saque = float(input("Informe o valor de saque: "))
        excedeu_limite = valor_saque > limite
        sem_saldo = valor_saque > saldo
        excedeu_saque = numero_saque > LIMITE_SAQUE

        if excedeu_limite:
            print("Valor excede o limite de saque!!")
        elif sem_saldo:
            print("Saldo insuficiente para saque!!")
        elif excedeu_saque:
            print("Excedeu o limite de saques diários!!")
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saque += 1
            print(f"Saque realizado com sucesso. Saldo atual R$ {saldo}")
        else:
            print("Operação falhou!!! Valor inválido")

    elif opcao == "e":
            print("____________________Extrato____________________\n")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print()
            print(f"Saldo:    R$ {saldo:.2f}\n")
            print("_______________________________________________")

    elif opcao == "q":
        print("Obrigado por confiar no nosso sistema")
        break
    else:
        print("Operação inválida, por favor selecione uma opção válida do menu.")