from Tarea5.Gasto import Gasto
from Tarea5.TipoGasto import TipoGasto
from Tarea5.TipoPago import TipoPago
from Tarea5.Conversor import ConversorDivisas
from datetime import date

class ControladorGastos:
    def __init__(self, viaje):
        self.viaje = viaje

    def crear_gasto(self, fecha: str, valor: int, tipo_pago: TipoPago, tipo_gasto: TipoGasto, moneda: str):
        return Gasto(fecha, valor, tipo_pago, tipo_gasto,moneda)

    def registrar_gasto(self, fecha, valor, tipo_pago, tipo_gasto, moneda):

        valor_pesos = ConversorDivisas.convertir_a_pesos(valor,moneda)

        if valor_pesos > self.viaje.presupuesto_diario:
            raise ValueError("El valor del gasto excede el presupuesto diario del viaje.")


        nuevo_gasto = self.crear_gasto(fecha, valor_pesos, tipo_pago, tipo_gasto,moneda)


        self.viaje.agregar_gasto(nuevo_gasto)


        diferencia = self.calcular_diferencia_presupuesto()


        return diferencia

    def calcular_diferencia_presupuesto(self):
        total_gastos = sum(gasto.valor for gasto in self.viaje.obtener_gastos())
        diferencia = self.viaje.presupuesto_diario - total_gastos
        return diferencia
