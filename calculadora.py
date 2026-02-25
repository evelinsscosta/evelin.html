def calculadora(num1, num2, operacao):
    if operacao == "soma":
        return num1 + num2
    elif operacao == "subtracao":
        return num1 - num2
    elif operacao == "multiplicacao":
        return num1 * num2
    elif operacao == "divisao":
        if num2 != 0:
            return num1 / num2
        else:
            return 0
    else:
        return 0


# Exemplos de uso:
print(calculadora(10, 5, "soma"))            # 15
print(calculadora(10, 5, "subtracao"))       # 5
print(calculadora(10, 5, "multiplicacao"))   # 50
print(calculadora(10, 5, "divisao"))         # 2.0
print(calculadora(10, 5, "potencia"))        # 0 (operação inexistente)