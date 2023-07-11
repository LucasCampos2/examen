import os
import numpy as np
import examen_funciones as fb


edif1 = np.zeros([10, 4],          type(int))
edif2= np.zeros([10, 4],          type(int))

fb.llenar_edif(edif1)
fb.llenar_edif(edif2)

recaudado = 0
recaudadoa=0
recaudadob=0
recaudadoc=0
recaudadod=0
cantA=0
cantB=0
cantC=0
cantD=0
p=1
while True:
    os.system("cls")
    os.system("cls")
    print("Inmobilaria Casa Feliz ")
    print("")
    print("1) -> Comprar Departamento")
    print("2) -> Mostrar Departamentos Disponibles")
    print("3) -> Ver Listado de Compradores")
    print("4) -> Mostrar Ganancias Totales")
    print("5) -> Salir")
    print()    
    op = fb.menu()

    if op == 1:

        recaudado = fb.comprar_dep(edif1, recaudado,recaudadoa,recaudadob,recaudadoc,recaudadod,cantA,cantB,cantC,cantD)
        recaudadoa = fb.comprar_dep(edif1, recaudado,recaudadoa,recaudadob,recaudadoc,recaudadod,cantA,cantB,cantC,cantD)
        recaudadob = fb.comprar_dep(edif1, recaudado,recaudadoa,recaudadob,recaudadoc,recaudadod,cantA,cantB,cantC,cantD)
        recaudadoc = fb.comprar_dep(edif1, recaudado,recaudadoa,recaudadob,recaudadoc,recaudadod,cantA,cantB,cantC,cantD)
        recaudadod = fb.comprar_dep(edif1, recaudado,recaudadoa,recaudadob,recaudadoc,recaudadod,cantA,cantB,cantC,cantD)
        cantA = fb.comprar_dep(edif1, recaudado,recaudadoa,recaudadob,recaudadoc,recaudadod,cantA,cantB,cantC,cantD)
        cantB = fb.comprar_dep(edif1, recaudado,recaudadoa,recaudadob,recaudadoc,recaudadod,cantA,cantB,cantC,cantD)
        cantC = fb.comprar_dep(edif1, recaudado,recaudadoa,recaudadob,recaudadoc,recaudadod,cantA,cantB,cantC,cantD)
        cantD = fb.comprar_dep(edif1, recaudado,recaudadoa,recaudadob,recaudadoc,recaudadod,cantA,cantB,cantC,cantD)
        os.system("cls")



    elif op == 4:
        if recaudado is None:
            recaudado = 0
        else:
                if(op==4):
                    print("Tipo","||","||","Total")
                    print("A         ",cantA,recaudadoa)
                    print("B         ",cantB,recaudadob)
                    print("C         ",cantC,recaudadoc)
                    print("D         ",cantD,recaudadod)
                    print(recaudado)

        os.system("pause")


        

