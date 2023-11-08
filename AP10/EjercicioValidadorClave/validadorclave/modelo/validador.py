# TODO: Implementa el código del ejercicio aquí
#'''
from abc import ABC
from abc import abstractclassmethod
from modelo.errores import *


class ReglaValidacion(ABC):
    def __init__(self,longitud_esperada:int) -> None:
        super().__init__()
        self._longitud_esperada=longitud_esperada

    @abstractclassmethod
    def es_valida(self,clave:str):
        pass

    def _validar_longitud(self,clave:str)->bool:
        return len(clave)>self._longitud_esperada

    def _contiene_mayuscula(self, clave:str)->bool:
        return not clave.islower()
    #    for caracter in clave:
    #        if caracter.isupper():
    #            return True
    #    return False
    
    def _contiene_minuscula(self, clave:str)->bool:
        return not clave.isupper()
    #    for caracter in clave:
    #        if caracter.islower():
    #            return True
    #    return False
    
    def _contiene_numero(self, clave:str):
        for caracter in clave:
            if caracter.isdigit():
                return True
            return False


class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self, longitud_esperada: int) -> None:
        super().__init__(longitud_esperada)

    def contiene_caracter_especial(self, clave:str)->bool:
        caracteres_especiales="@_#$%"
        for caracter in clave:
            if caracter in caracteres_especiales:
                return True
        return False

    def es_valida(self, clave:str)->bool:
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError()
        elif not self._continene_mayuscula(clave):
            raise NoTieneLetraMayusculaError()
        elif not self._contiene_minuscula(clave):
            raise NoTieneLetraMinusculaError()
        elif not self._contiene_numero(clave):
            raise NoTieneNumeroError()
        elif not self.contiene_caracter_especial():
            raise NoTieneCaracterEspecialError
        else:
            return True
        


class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self, longitud_esperada: int) -> None:
        super().__init__(longitud_esperada)

    def contiene_calisto(self, clave:str)->bool:
        indice=clave.lower().find('calisto')
        if indice != -1 and not clave[indice:indice+8].isupper():
            mayusculas=sum(1 for char in clave if char.isupper())
            if mayusculas>=2:
                return True
        else:
            return False
        
    def es_valida(self, clave:str)->bool:
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError()
        elif not self._contiene_numero(clave):
            raise NoTieneNumeroError()
        elif not self.contiene_calisto(clave):
            raise NoTienePalabraSecretaError()

class Validador():
    def __init__(self, regla:ReglaValidacion) -> None:
        self.regla=regla

    def es_valida(self,clave:str)->bool:
        self.regla.es_valida(clave)