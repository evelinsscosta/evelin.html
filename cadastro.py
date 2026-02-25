while True:
    nome = input("Digite seu nome completo: ")

    try:
        ano = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))
    except ValueError:
        print("Erro: Você precisa digitar um número válido.")
        continue

    if ano < 1922 or ano > 2021:
        print("Erro: O ano deve estar entre 1922 e 2021.")
        continue

    break

idade = 2022 - ano

print(f"\nNome: {nome}")
print(f"Em 2022 você completou ou completará {idade} anos.") 