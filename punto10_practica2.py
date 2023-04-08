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

A = list()
B = list()

def puntoa(A):
    A=list(zip(nombres.splitlines(),notas_1,notas_2))
    print(A)


def puntob(B):
    prom = [(notas_1 + notas_2)/2 for notas_1,notas_2 in zip(notas_1, notas_2)]
    b = list(zip(nombres, prom))
    print(b)
    return b    
    
def puntoc(B):
    cont = 0
    prom = 0
    for i in B:
        cont = cont + 1
        prom = prom + i[1]
    prom = prom / cont
    print(prom)
        
def puntoD(B):       
    maximo = 0
    nom_max = ""
    for i in B:
        if (i[1] > maximo):
            nom_max = i[0]
            maximo = i[1]
    print(f"el alumno con mayor promedio es: {nom_max} con un promedio de {maximo}")

def puntoE(B):
    minimo = 9999
    nom_min = ""
    for i in B:
        if (i[1] < minimo):
            nom_min = i[0]
            minimo = i[1]
    print(f"el alumno con el promedio mas bajo:{nom_min} con un promedio de {minimo}")

puntoa(A)
puntob(B)
puntoc(B)
puntoD(B)
puntoE(B)    