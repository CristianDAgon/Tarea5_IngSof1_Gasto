from Tarea5.TipoPago import TipoPago
from datetime import date


class Viaje:
    def __init__(self, destino: str, fecha_inicio: date, fecha_final: date, presupuesto_diario: int):
        self.destino = destino
        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final
        self.presupuesto_diario = presupuesto_diario
        self.gastos = []

    def agregar_gasto(self, gasto):
        self.gastos.append(gasto)

    def obtener_gastos(self):
        return self.gastos


    def generar_reporte(self):
        """
        Metodo que sera utilizado por la propia clase viaje
        genera un reporte del viaje, donde
        necesitaremos los diferentes datos tanto del viaje ,
        los gastos realizado y el total
        ademas por pantalla mostramos la diferencia con el presupuesto
        :return: reporte con toda la informacion necesaria
        """
        reporte = "------------Reporte de Gastos --------------\n"
        reporte += f"Destino: {self.destino}\n"
        reporte += f"Fecha Inicio: {self.fecha_inicio}\n"
        reporte += f"Fecha Final: {self.fecha_final}\n"
        reporte += ("\n")
        reporte += "Gastos por día (separados por efectivo y tarjeta):\n"

        # Creamos diccionario con clave fecha y su valores correspondientes
        gastos_por_dia = {}
        for gasto in self.gastos:
            if gasto.fecha not in gastos_por_dia:
                # iniciamos por fecha e inicializamos sus gastos en 0
                gastos_por_dia[gasto.fecha] = {'efectivo': 0, 'tarjeta': 0}

            # Sumar  a cada tipo de pago su valor correspondiente en el dia
            if gasto.tipo_pago == TipoPago.EFECTIVO:
                gastos_por_dia[gasto.fecha]['efectivo'] += gasto.valor
            else:
                gastos_por_dia[gasto.fecha]['tarjeta'] += gasto.valor

        # Generamos el reporte , organizamos por fecha con el sorted
        for fecha, gastos in sorted(gastos_por_dia.items()):
            total_dia = gastos['efectivo'] + gastos['tarjeta']
            reporte += f"Fecha: {fecha}:\n"
            reporte += f"  Efectivo: {gastos['efectivo']}\n"
            reporte += f"  Tarjeta: {gastos['tarjeta']}\n"
            reporte += f"  Total: {total_dia}\n"

        return reporte
