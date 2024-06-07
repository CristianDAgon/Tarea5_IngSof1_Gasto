from enum import Enum

#Clase que se encargara de tener los diferentes tipos de gasto
class TipoGasto(Enum):
    TRANSPORTE = "Transporte"
    ALOJAMIENTO = "Alojamiento"
    ALIMENTACION = "Alimentación"
    ENTRETENIMIENTO = "Entretenimiento"
    COMPRAS = "Compras"