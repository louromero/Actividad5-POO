import csv
from Alumno import Alumno

def imprimir():
    print(" ")
    print("----------MENU------------")
    print("1. Porcentaje de Inasistencia")
    print("2. Modificar cantidad maxima de inasistencias permitidas")
    print("0. Salir")
    print(" ")

def testAlumno(listaAlumnos):
    archivo=open('alumnos.csv')
    reader=csv.reader(archivo,delimiter=',')
    for fila in reader:
        nombreAlumno=fila[0]
        anio=int(fila[1])
        division=fila[2]
        inasistencia=int(fila[3])
        unAlumno=Alumno(nombreAlumno,anio,division,inasistencia)
        listaAlumnos.append(unAlumno)

def menu():
    band=True
    while band:
        imprimir()
        opcion=int(input("Ingrese una opcion: "))
        if opcion==1:
            year=int(input("Ingrese anio: "))
            div=(input("Ingrese division (EN MAYUSCULA): "))
            print(" ")
            print("ALUMNO \t\t\t\t PORCENTAJE DE INASISTENCIA")
            for i, Alumno in enumerate(listaAlumnos):
                #print("si entra al for")
                if Alumno.getInasistencia()>Alumno.getInasistenciaMaxima() and Alumno.getAnio()==year and Alumno.getDivision()==div:
                    print("{}\t\t{}%".format(Alumno.getNombreAlumno(),Alumno.getPorcentaje()))

        elif opcion==2:
            nuevo=int(input("Nueva cantidad de inasistencias permitidas: "))
            Alumno.modificarInasistencias(nuevo)
            print(" ")
            print("Cantidad permitida de inasistencias: {}".format(Alumno.getInasistenciaMaxima()))

        elif opcion==0:
            print("Chau :) ")
            band=False

        else:
            print("Opcion no valida")


if __name__=='__main__':
    listaAlumnos=[]
    testAlumno(listaAlumnos)
    menu()