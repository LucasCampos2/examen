import os

def llenar_edif (edif1):
    cont = 1
    for i in range(10):
        for j in range(4):
            edif1[i, j] = cont
            cont += 1

def menu():
    while True:
        try:
            op = int(input("                Elija Opción: _"))
            if op > 0 and op < 6:
                return op
        except ValueError:
            print("")

def mostrarDisponibles(edif1):
    os.system("cls")
    for i in range(10):
        print("\n")
        for j in range(4):
            if(j==1):
                print("\t",edif1[i,j], end="        ")
            else:
                print("\t",edif1[i,j], end="    ")
    print("\n\n")

def comprar_dep(edif1, recaudado,recaudadoa,recaudadob,recaudadoc,recaudadod,cantA,cantB,cantC,cantD):
    os.system("cls")
    mostrarDisponibles(edif1)
    while True:
        try:
            op=int(input("escoja el pasaje que desea cancelar: "))
            if op > 0 and op < 41:
                break
        except ValueError:
            print("")
    for i in range(1):
        if op == edif1[i, 0]:
            edif1[i, 0] = 0
            recaudado += 3800
            recaudadoa += 3800
            cantA+=1
            os.system("pause")
            return recaudado
        elif op == edif1[i, 1]:
            edif1[i, 1] = 0
            recaudado += 3000
            recaudadob += 3000
            cantB+=1
            return recaudado
        elif op == edif1[i, 2]:
            edif1[i, 2] = 0
            recaudado += 2800
            recaudadoc += 2800
            cantC+=1
            os.system("pause")
            return recaudado
        elif op == edif1[i, 3]:
            edif1[i, 3] = 0
            recaudado += 3500
            recaudadod += 3500
            cantD+=1
            os.system("pause")
            return recaudado
        else:
            print("el asiento ya fue compreado")
            recaudado += 0
            os.system("pause")
            return recaudado
    print("Ingresando rut  ",p)
    rut=0
    while(rut==0):
        rut=input("Ingrese su RUN , sin digito verificador ")
        if(len(rut)!=8):
            print("por favor ingrese su RUN")
            rut=0
        os.system("pause")
    os.system("pause")
    print("Gracias por su compra")
    p+=1


