# Ex1
lista_times = ['Flamengo', 'Cruzerio', 'Palmeiras', 'Barcelona', 'Botafogo']

# a) 3 primeiros colocados
print(lista_times[:3])

# b) últimos 2 colocados
print(lista_times[-2:])

# c) times em ordem alfabética (sem alterar a ordem original)
print(sorted(lista_times))

# d) posição do Barcelona (na ordem original)
pos_barcelona = None
for i in range(len(lista_times)):
    if lista_times[i].lower() == "barcelona":
        pos_barcelona = i + 1
        break
print(pos_barcelona if pos_barcelona else "Barcelona não está na lista")


# Ex2
conjunto_loja1 = {"iPhone", "Samsung", "Xiaomi", "Motorola"}
conjunto_loja2 = {"Samsung", "Xiaomi", "OnePlus", "Nokia"}

print("Modelos disponíveis no total:", conjunto_loja1 | conjunto_loja2)
print("Modelos disponíveis em ambas as lojas:", conjunto_loja1 & conjunto_loja2)


# Ex3
nome = str(input("Digite o nome do aluno: "))
media = float(input("Digite a media do aluno: "))

dicionario_aluno = {"Nome": nome, "Media": media}
dicionario_aluno["Situacao"] = "AP" if media >= 50 else "RP"

print(dicionario_aluno)


# Ex4
mais_pesada = ""
mais_leve = ""
peso_maior = 0
peso_menor = 0

for i in range(3):
    nome = input("Nome: ")
    peso = float(input("Peso: "))

    if i == 0:
        mais_pesada = mais_leve = nome
        peso_maior = peso_menor = peso
    else:
        if peso > peso_maior:
            mais_pesada = nome
            peso_maior = peso
        if peso < peso_menor:
            mais_leve = nome
            peso_menor = peso

print("Mais pesada:", mais_pesada)
print("Mais leve:", mais_leve)


# Ex5
n = int(input("\nQuantas pessoas deseja cadastrar? "))
soma_idades = 0
mulheres_menor_20 = 0

for i in range(n):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").upper()

    soma_idades += idade

    if sexo == "F" and idade < 20:
        mulheres_menor_20 += 1

media_idades = soma_idades / n
print("\nMédia de idade do grupo:", media_idades)
print("Mulheres com menos de 20 anos:", mulheres_menor_20)
