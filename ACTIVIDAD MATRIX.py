#Primer problema
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[11, 12, 13],
           [14, 15, 16],
           [17, 18, 19]]
resultado = []

for num in range(len(matrix1)):
    nuevo = []
    for element in range(len(matrix1[0])):
        nuevo.append(matrix1[num][element] + matrix2[num][element])

    resultado.append(nuevo)

for nuevo in resultado:
    print(nuevo)

#Segundo problema
matrix1 = [[1, 2, 3],
           [4, 5, 6], 
           [7, 8, 9]]

matrix2 = [[11, 12, 13],
           [14, 15, 16],
           [17, 18, 19]]
resultado = []

for num in range(len(matrix1)):
    nuevo = []
    for element in range(len(matrix1[0])):
        nuevo.append(matrix1[num][element] * matrix2[num][element])

    resultado.append(nuevo)

for nuevo in resultado:
    print(nuevo)

#Tercer problema
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

nuevaMatrix = []

for i in range(len(matrix[0])):
    filaCambio = []
    for j in range(len(matrix)):
      
        filaCambio.append(matrix[j][i])
 
    nuevaMatrix.append(filaCambio)

for fila in nuevaMatrix:
    print(fila)

#Cuarto problema
matrix = [
    [8, 1, 6], 
    [3, 5, 7],
    [4, 9, 2]
]

nueva = [0, 0, 0, 0, 0, 0, 0, 0]

ent = int(-1)
for i in range(0, 3):
    ent = ent + 1
    for j in range(0, 3):
        nueva[ent] = nueva[ent] + matrix[i][j]        
        nueva[ent + 3] = nueva[ent + 3] + matrix[j][i]  

for i in range(0, 3):
    nueva[6] = nueva[6] + matrix[i][i]          
    nueva[7] = nueva[7] + matrix[i][2 - i]      

part_2 = True
i = 0
while part_2 and i < 7:
    if nueva[i] != nueva[i + 1]:
        part_2 = False
    i += 1

if part_2:
    print("La matriz brindada es magica")
else:
    print("La matriz brindada no es magica")

for i in range(0, 8):
    print(str(nueva[i])+"\t")