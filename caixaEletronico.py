import time

valor = 0
saldo = 0
confirm = 0




while True:
    print("QUAL DESSAS OPERAÇÕES DESEJA REALIZAR?\n")

    operacao = int(input("Depósito press 1 \nSaque press 2 \nSaldo press 3 \nSair press 4 \n"))

    if operacao == 1:
      valor = float(input("Qual valor deseja depositar: "))
      confirm = input("\nDigite Y para confirmar o deposito ou N para cancelar: \n")
      if confirm == "y" or confirm == "Y":
        saldo = saldo + valor
        print("\nDepositando, aguarde...\n")
        time.sleep(1)
        print("\nDeposito Realizado com sucesso!!\n")
        continue
      elif confirm != "N" or confirm != "n":
          print("\nCancelando...\n")
          time.sleep(1)
          print("\nOperação cancelada!!\n")
          break
      else:
        print("\nOperação Invalida!!\n")

    elif operacao == 2:
      valor = float(input("\nQual valor deseja sacar: "))
      if saldo >= valor:
          confirm = input("\nDigite Y para confirmar o saque ou N para cancelar: \n")
          if confirm == "y" or confirm == "Y":
              saldo = saldo - valor
              print("\nRealizando o saque, aguarde...\n")
              time.sleep(1)
              print("\nSaque Realizado com sucesso!!\n")
              continue
          elif confirm == "N" or confirm == "n":
              print("Cancelando...")
              time.sleep(1)
              print("\nOperação Cancelada!\n")
              break
          else:
            print("\nOperação inválida, tente novamente!!\n")
      else:
        print("\nSaldo insuficiente!\n")
        continue

    elif operacao == 3:
      print("\nVerificando seu saldo, aguarde...\n")
      time.sleep(1)
      print(f"\nSeu saldo é de: R${saldo}\n")

    elif operacao == 4:
        confirm = input("\nDeseja realmente sair? press Y para sair N para permanecer: ")
        if confirm == "y" or confirm == "Y":
          print("\nSaindo...\n")
          time.sleep(1)
          print("Finalizado! Obrigado, volte sempre!")
          break
        else:
          confirm == "n" or confirm == "N"
          continue

    else:
      print("operacao invalida")





