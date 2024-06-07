import os
import logging
from Tarea5.ArchivoException import ArchivoException

class Archivo:
    @staticmethod
    def guardar_reporte(nombre_archivo, contenido):
        """
        Metodo que guarda en el escritorio el reporte de un viaje
        :param nombre_archivo: nombre que tendra el archito
        :param contenido:  Reporte del viaje
        """
        escritorio = os.path.join(os.path.expanduser("~"), "Desktop")
        ruta_archivo = os.path.join(escritorio, nombre_archivo)
        try:
            with open(ruta_archivo, "w") as archivo:
                archivo.write(contenido)
            logging.info(f"Reporte guardado exitosamente en '{ruta_archivo}'.")
        except ArchivoException as e:
            logging.error(f"Error al guardar el reporte en el archivo '{ruta_archivo}': {str(e)}")

