from random import choice, randrange
from datetime import datetime
# Operadores posibles
operators = ["+", "-", "*", "/"]
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
cont = 0

for i in range(0, times):
# Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10) 
    operator = choice(operators)
    correcto = False
    if ((operator == "/") & (number_2 == 0)):
        number_2 = randrange(1,10)
# Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
# Le pedimos al usuario el resultado
    result = int(input("resultado: "))
    if operator == "+":
        correcto = (result == (number_1 + number_2))
    elif operator == "-":
        correcto = result == (number_1 - number_2)   
    elif operator == "*":
        correcto = result == (number_1 * number_2)  
    else:
        correcto = result == (number_1 // number_2)  
    if correcto == True:
        print("Correcto")
        cont += 1
    else:
        print("Mal")
    

    # Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")
print(f"\n Acertaste {cont} veces")
print(f"\n Erraste {times - cont} veces")