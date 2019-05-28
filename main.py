from condicionais import Condicionais

print("Olá! Vamos calcular seu IMC!")


Peso = float(input("Qual é o seu peso?"))
Altura = float(input("Qual é a sua altura?"))

IMC = Peso / (Altura * Altura)

Cond = Condicionais(IMC)

print("Seu IMC é: {:.2f}".format(Cond.IMC))







