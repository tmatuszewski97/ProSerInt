def temperature_calc(temperature, temperature_type):
    temperature = float(temperature)
    if temperature_type == 'F':
        temperature = temperature * 1.8 + 32
    elif temperature_type == 'R':
        temperature = (temperature + 273.15) * 1.8
    elif temperature_type == 'K':
        temperature = temperature + 273.15
    else:
        print("Wprowadziłeś inny znak niż wymagano!")
        return
    return temperature


temp = input("Wprowadź temperaturę (stopnie Celsjusza): ")
choose = input("Na jaką jednostkę chcesz ją przeliczyć? Wprowadź:\n"
               "F - Fahrenheit\nR - Rankine\nK - Kelvin\nWprowadzanie: ")
new_temp = temperature_calc(temp, choose)
print('Wynik:', new_temp)
