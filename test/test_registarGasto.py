import unittest
from unittest import TestCase
from datetime import date
from Tarea5.Viaje import Viaje
from Tarea5.ControlGasto import ControladorGastos
from Tarea5.TipoPago import TipoPago
from Tarea5.TipoGasto import TipoGasto


class TestGasto(TestCase):

    def test_registro_exitoso(self):
        fecha_inicio = date(2024, 6, 3)
        fecha_final = date(2024, 6, 10)
        presupuesto_diario = 100000
        mi_viaje = Viaje("Madrid", fecha_inicio, fecha_final, presupuesto_diario)
        controlador = ControladorGastos(mi_viaje)

        fecha_gasto = date(2024, 6, 3)
        valor_gasto = 10
        tipo_pago_gasto = TipoPago.EFECTIVO
        tipo_gasto = TipoGasto.TRANSPORTE
        moneda = "USD"

        # Registrar el gasto, por medio de una resta con presupuesto validamos el registro
        presupuesto_actual = controlador.calcular_diferencia_presupuesto()
        controlador.registrar_gasto(fecha_gasto, valor_gasto, tipo_pago_gasto, tipo_gasto, moneda)
        presupuesto_con_gasto = controlador.calcular_diferencia_presupuesto()

        # Verificar que la diferencia se ha reducido después de registrar el gasto
        self.assertTrue(presupuesto_actual > presupuesto_con_gasto)

    def test_registro_moneda_no_soportada(self):
        fecha_inicio = date(2024, 6, 1)
        fecha_final = date(2024, 6, 10)
        presupuesto_diario = 100000
        mi_viaje = Viaje("Paris", fecha_inicio, fecha_final, presupuesto_diario)
        controlador = ControladorGastos(mi_viaje)

        fecha_gasto = date(2024, 6, 1)
        valor_gasto = 50
        tipo_pago_gasto = TipoPago.EFECTIVO
        tipo_gasto = TipoGasto.TRANSPORTE
        moneda = "CNY"

        # Intentar registrar el gasto con una moneda no soportada
        with self.assertRaises(ValueError):
            controlador.registrar_gasto(fecha_gasto, valor_gasto, tipo_pago_gasto, tipo_gasto, moneda)

    def test_presupuesto_insuficiente(self):

        fecha_inicio = date(2024, 6, 1)
        fecha_final = date(2024, 6, 10)
        presupuesto_diario = 100
        mi_viaje = Viaje("Miami", fecha_inicio, fecha_final, presupuesto_diario)
        controlador = ControladorGastos(mi_viaje)

        fecha_gasto = date(2024, 6, 1)
        valor_gasto = 1000
        tipo_pago_gasto = TipoPago.EFECTIVO
        tipo_gasto = TipoGasto.TRANSPORTE
        moneda = "USD"

        # Intentar registrar el gasto con un presupuesto insuficiente
        with self.assertRaises(ValueError):
            controlador.registrar_gasto(fecha_gasto, valor_gasto, tipo_pago_gasto, tipo_gasto, moneda)
