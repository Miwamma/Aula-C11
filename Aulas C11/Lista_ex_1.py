import math

#Ex1 
nome = input("Qual seu nome? ")

print(nome.upper())
print(nome.lower())
print(len(nome))

#Ex2 
numero_tabuada = int(input("Voce quer a tabuada de qual número? "))
limite = int(input("Qual o limite que voce quer? "))

for i in range(1, limite+1):
    print(numero_tabuada*i)

#Ex3
sexo = str(input("Qual o seu sexo, digite M para masculino ou F para feminino: ")).upper()

while sexo!="M" and sexo!="F":
    print("Escreva novamente")
    sexo = str(input("Digite novamente um sexo M ou F ")).upper()


if sexo == "M":
    print("Masculino")
elif sexo == "F":
    print("Feminino")
else:
    print("Digite novamente")

#Ex4
distancia = float(input("Qual a distancia da viagem? "))

if distancia > 200:
    preco = distancia*0.45
    print(f"O valor é de R$: {preco:.2f}")

else:
    preco = distancia*0.50
    print(f"O valor é de R$: {preco:.2f}")

#Ex5
numero_ex5 = int(input("Digite um numero entre 1000 e 9999: "))

if 1000<= numero_ex5 <=9999:
    milhar = numero_ex5//1000
    centena = (numero_ex5%1000)//100
    dezena = (numero_ex5%100)//10
    unidade = numero_ex5%10

    print(f"Milhar = {milhar}")
    print(f"Centena = {centena}")
    print(f"Dezena = {dezena}")
    print(f"Unidade = {unidade}")


#Ex6
decimal = float(input("Insira um numero decimal: "))

print(f"A raiz é {math.sqrt(decimal)}")
print(f"Depois de aplicar a função teto temos: {math.ceil(decimal)}")
print(f"Depois de aplicar a função chao temos: {math.floor(decimal)}")
print(f"Sua parte inteira é: {math.trunc(decimal)}")