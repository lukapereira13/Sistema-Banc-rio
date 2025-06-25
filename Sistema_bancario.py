# Sistema-Bancario
MENU = """

 [1] Deposito
 [2] Sacar
 [3] Extrato
 [0] Sair

 => """

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:

       opcao = input(MENU)

       if opcao == "1":
          valor = float(input("Informe o valor do Deposito:"))

          if valor > 0:
               saldo += valor
               extrato += f"deposito:R${valor:.2f}\n"
               
          else:
            print("Operação falhou! O valor informado é invalido.")

       elif opcao == "2":
        valor = float(input("Informe o valor do saque:"))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação falhou! Saldo Insuficiente.")

        elif excedeu_limite:
            print("Operação Negada! Valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação Negada! Número máximo de saque excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"saque:R${valor :.2f}\n"
            numero_saques += 1

        else:
            print("Operação Negada! Valor invalido!")

       elif opcao == "3":
           print("\n ======EXTRATO======")
           print("Não foram realizados movimentações." if not extrato else extrato)
           print(f"\nsaldo: R${saldo:.2f}")
           print("==========================")
        
       elif opcao == "0":
           break
       
       else:
           print("Operação Negada, favor selecionar a operação desejada!!")
