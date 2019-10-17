# Zadanie 5


class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def difference(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            print("Nie można dzielić przez zero!")
            return
        else:
            return self.a / self.b


# Zadanie 6


class ScienceCalculator(Calculator):
    def power(self):
        return self.a ** self.b


number1 = float(input("Wprowadź pierwszą liczbę: "))
number2 = float(input("Wprowadź drugą liczbę: "))
obj = Calculator(number1, number2)
new_obj = ScienceCalculator(number1, number2)
print("Dodawanie:", obj.add())
print("Odejmowanie:", obj.difference())
print("Mnożenie:", obj.multiply())
print("Dzielenie:", obj.divide())
print("Potęgowanie:", new_obj.power())
