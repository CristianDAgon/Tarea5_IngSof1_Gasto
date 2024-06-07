from datetime import date
from Tarea5.Viaje import *
from Tarea5.ControlGasto import *
from Tarea5.Archivo import Archivo  # Asegúrate de importar la clase Archivo correctamente

def main():
    # Creamos un viaje
    fecha_inicio = date(2024, 6, 1)
    fecha_final = date(2024, 6, 10)
    presupuesto_diario = 200000  # Presupuesto en pesos colombianos por día
    mi_viaje = Viaje("Paris", fecha_inicio, fecha_final, presupuesto_diario)

    # A la clase control le añadimos ese viaje
    controlador = ControladorGastos(mi_viaje)

    #Creamos un gasto dentro de alguna fecha del viaje
    fecha_gasto1 = date(2024, 6, 1)
    valor_gasto1 = 20
    tipo_pago_gasto1 = TipoPago.EFECTIVO
    tipo_gasto1 = TipoGasto.TRANSPORTE
    moneda1 = "USD"

    #Registramos el gasto en la clase controladora
    controlador.registrar_gasto(fecha_gasto1, valor_gasto1, tipo_pago_gasto1, tipo_gasto1, moneda1)

    #Creamos un segundo gasto para el mismo dia
    fecha_gasto2 = date(2024, 6, 1)
    valor_gasto2 = 15
    tipo_pago_gasto2 = TipoPago.TARJETA
    tipo_gasto2 = TipoGasto.ALIMENTACION
    moneda2 = "USD"
    controlador.registrar_gasto(fecha_gasto2, valor_gasto2, tipo_pago_gasto2, tipo_gasto2, moneda2)



    # Generar un reporte por día
    reporte_por_dia = mi_viaje.generar_reporte()
    print(reporte_por_dia)  # Imprimir el reporte en la consola

    presupuesto_dia = mi_viaje.presupuesto_diario
    print(f"Presupuesto del dia: {presupuesto_dia}")
    print("-----------------------------------------------------")


    # Calcular la diferencia de presupuesto
    diferencia = controlador.calcular_diferencia_presupuesto()
    print("------------------------------------------------------")
    print(f"Presupuesto actualizado: {diferencia}")



    # Guardar el reporte en un archivo
    nombre_archivo = "reporte_viaje.txt"
    Archivo.guardar_reporte(nombre_archivo, reporte_por_dia)

if __name__ == "__main__":
    main()

