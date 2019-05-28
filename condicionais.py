class Condicionais:

    def __init__(self, imc):
        self.IMC = imc


        if (self.IMC <= 18.5):
            print("Você está abaixo do peso!")

        if (self.IMC >= 18.5 and self.IMC <= 24.9):
            print("Você está no peso correto! Parabéns!")

        if (self.IMC >=25 and self.IMC <=29.9):
            print("Você está com sobre peso. Fique atento e cuide-se.")

        if (self.IMC >= 30 and self.IMC <= 34.9):
            print("Você está com obesidade grau 1. É bom se 9cuidar.")

        if (self.IMC >=35 and self.IMC <=39.9):
            print("Você está com obesidade grau 2. Cuide-se.")

        if (self.IMC >= 40):
            print("Você está com obesidade grau 3. Você precisa, urgentemente, se cuidar.")
