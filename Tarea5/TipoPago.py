from enum import Enum

#Clase que se encargara de tener los diferentes tipos de pago
class TipoPago(Enum):
    EFECTIVO = "Efectivo"
    TARJETA = "Tarjeta"