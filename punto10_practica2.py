nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]


def puntoa(nombres,notas_1,notas_2):
    nombres_n = nombres.replace(",","")
    nombres_n = nombres_n.replace("'","")
    nombres_n = nombres_n.split()
    A=list(zip(nombres_n,notas_1,notas_2))
    print(A)
    return A

def puntob(A):
    promedios = list(map(lambda x: (x[0], sum(x[1:]) / len(x[1:])), A))
    print(promedios)
    return promedios

def puntoc(B):
    total = 0
    cont = 0
    for i in B:
        total += i[1]
        cont += 1
    total = total / cont
    print (f"promedio total: {total}") 

def puntod(B):
    promedio_bajo = min(B,key=lambda x: x[1])
    print(f"promedio mas bajo: {promedio_bajo[0]}, {promedio_bajo[1]}")

def puntoe(B):
    promedio_alto = max(B,key=lambda x: x[1])
    print(f"promedio mas alto: {promedio_alto[0]}, {promedio_alto[1]}")


pa = puntoa(nombres,notas_1,notas_2)
pro =  puntob(pa)
puntoc(pro)
puntod(pro)
puntoe(pro)
