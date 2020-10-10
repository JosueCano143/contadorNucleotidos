# Author: Josue Salvador Cano Martinez
# ID: A00829022
# Date: 31/03/2020
# Program: Nucleótidos

# Inicialización de acumuladores
aAccumulator = ""
tAccumulator = ""
cAccumulator = ""
gAccumulator = ""
# Inicialización de contadores
aCount = 0
tCount = 0
cCount = 0
gCount = 0

# Eliminar los saltos de línea del archivo
vectorFile = ''
file = open ('apc.fasta', 'r');
for iK in file.readlines():
    line1 = iK.rstrip('\n');
    vectorFile += line1;
file.close();
length = len(vectorFile)

# Inicialización de variables controladoras del for
variable = ''
longitud = 0
aNumber = 0
tNumber = 0
cNumber = 0
gNumber = 0
contA = 1
tryA = ""
contT = 1
tryT = ""
contC = 1
tryC = ""
contG = 1
tryG = ""
# Ciclo for que permite contar el total de cada nucleótido
for iK in vectorFile:
    if iK == 'A':
        aCount = aCount + 1
        if variable == 'A':
            aAccumulator = aAccumulator + 'A'
            longitud = len(aAccumulator)+1
            if longitud > aNumber:
                aNumber = longitud
        else:
            aAccumulator = ''
        if aAccumulator > tryA:
            tryA = aAccumulator
        if aAccumulator == tryA:
            contA += 1
        else:
            contA = 1
         
    elif iK == 'T':
        tCount = tCount + 1
        if variable == 'T':
            tAccumulator = tAccumulator + 'T'
            longitud = len(tAccumulator)+1
            if longitud > tNumber:
                tNumber = longitud
        else:
            tAccumulator = ''
        if tAccumulator > tryT:
            tryT = tAccumulator
        if tAccumulator == tryT:
            contT += 1
        else:
            contT = 1
    elif iK == 'C':
        cCount = cCount + 1
        if variable == 'C':
            cAccumulator = cAccumulator + 'C'
            longitud = len(cAccumulator)+1
            if longitud > cNumber:
                cNumber = longitud
        else:
            cAccumulator = ''
        if cAccumulator > tryC:
            tryC = cAccumulator
        if cAccumulator == tryC:
            contC += 1
        else:
            contC = 1
    elif iK == 'G':
        gCount = gCount + 1
        if variable == 'G':
            gAccumulator = gAccumulator + 'G'
            longitud = len(gAccumulator)+1
            if longitud > gNumber:
                gNumber = longitud
        else:
            gAccumulator = ''
        if gAccumulator > tryG:
            tryG = gAccumulator
        if gAccumulator == tryG:
            contG += 1
        else:
            contG = 1
    variable = iK;
    

# Cálculo de porcentajes
aPercentage = float(aCount/length*100)
tPercentage = float(tCount/length*100)
cPercentage = float(cCount/length*100)
gPercentage = float(gCount/length*100)

# Impresión de resultados
print ("Porcentaje de A:", aPercentage,"%")
print("Cadena más larga con", aNumber, "A consecutivas, se repite ", contA, "veces")
print('\n')
print ("Porcentaje de T:", tPercentage,"%")
print("Cadena más larga con", tNumber, "T consecutivas, se repite ", contT, "veces")
print('\n')
print ("Porcentaje de C:", cPercentage,"%")
print("Cadena más larga con", cNumber, "C consecutivas, se repite ", contC, "veces")
print('\n')
print ("Porcentaje de G:", gPercentage,"%")
print("Cadena más larga con", gNumber, "G consecutivas, se repite ", contG, "veces")
