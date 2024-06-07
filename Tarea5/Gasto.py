from Tarea5.TipoGasto import TipoGasto
from Tarea5.TipoPago import TipoPago
from datetime import date

class Gasto:
    def __init__(self, fecha: date, valor: int, tipo_pago: TipoPago, tipo_gasto: TipoGasto, moneda: str):
        self.fecha = fecha  # Tipo str
        self.valor = valor  # Tipo float
        self.tipo_pago = tipo_pago  # Tipo TipoPago (enumeración)
        self.tipo_gasto = tipo_gasto  # Tipo TipoGasto (enumeración)
        self.moneda = moneda  # Tipo str

    def get_valor(self) -> int:
        return self.valor

    def get_fecha(self) -> str:
        return self.fecha

    def get_tipo_pago(self) -> TipoPago:
        return self.tipo_pago

    def get_tipo(self) -> TipoGasto:
        return self.tipo_gasto

    def get_moneda(self) -> str:
        return self.moneda

