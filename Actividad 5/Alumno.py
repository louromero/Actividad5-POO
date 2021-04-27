import csv

class Alumno:
    inasistenciaMaxima= 5
    clasesTotales=200

    __nombreAlumno=None
    __anio=None
    __division=None
    __inasistencia=None

    def __init__(self,nombreAlumno,anio,division,inasistencia):
        self.__nombreAlumno = nombreAlumno
        self.__anio = anio
        self.__division = division
        self.__inasistencia = inasistencia

    def getNombreAlumno(self):
        return self.__nombreAlumno

    def getAnio(self):
        return self.__anio

    def getDivision(self):
        return self.__division

    def getInasistencia(self):
        return self.__inasistencia

    def getPorcentaje(self):
        return (int(self.__inasistencia)*100)/Alumno.clasesTotales

    @classmethod
    def modificarInasistencias(self,nuevo):
        Alumno.inasistenciaMaxima = nuevo
        #self.inasistenciaMaxima = nuevo

    @classmethod
    def getInasistenciaMaxima(self):
        return self.inasistenciaMaxima