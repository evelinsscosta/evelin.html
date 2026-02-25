def calculadora():
    while True:
        print("\n===== CALCULADORA =====")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        opcao = input("Digite a opção: ")

        if opcao == "0":
            print("Programa encerrado.")
            break

        if opcao == "1":
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = num1 + num2
            print("Resultado:", resultado)

        elif opcao == "2":
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = num1 - num2
            print("Resultado:", resultado)

        elif opcao == "3":
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = num1 * num2
            print("Resultado:", resultado)

        elif opcao == "4":
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            if num2 != 0:
                resultado = num1 / num2
                print("Resultado:", resultado)
            else:
                print("Não é possível dividir por zero.")

        else:
            print("Essa opção não existe")

calculadora()