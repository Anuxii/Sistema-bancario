menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[9] Sair
 
=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
             print(f"\n\nSeu depósito de R${valor:.2f} foi concluído com sucesso!")
             saldo += valor
             extrato += f"Depósito: R$ {valor: .2f}\n"
             

        else:    
            print("Operação falhou. O valor informado é inválido.")
            
        

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        saldo_excedido = valor > saldo

        limite_excedido = valor > limite

        limite_saque_excedido = numero_saques >= LIMITE_SAQUES

        if saldo_excedido:
            print("Você não tem saldo suficiente.")

        elif limite_excedido:
            print("O valor do saque excede o limite diário")

        elif valor > 0:
            print(f"\n\nSeu saque no valor de R${valor:.2f} foi efetuado com sucesso!")
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1 
        else:
            print("O valor informado é inválido.")


    elif opcao == "3":
        print("\n============== Extrato ==============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("=======================================")

    elif opcao == "9":
        break    

    else:
        print("Operação inválida, por favor, selecione novamente a operação desejada.")        
