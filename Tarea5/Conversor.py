import logging
import requests


class ConversorDivisas:
    @staticmethod
    def convertir_a_pesos(valor, moneda):
        """
        Metodo que me permite convertir una moneda extranjera al valor en peso colombiano, este
        metodo a su vez utilizar una api la cual le permite obtener un valor ramdon entre 3500 y 4500
        simulando la moneda de USD o EUR
        :param valor:  valor a cambiar
        :param moneda:  tipo de moneda en el pais en el que esta
        :return:  el valor convertido a peso colombiano
        """
        if moneda == "USD":
            valor_convertido = ConversorDivisas._obtener_tasa_conversion()
        elif moneda == "EUR":
            valor_convertido = ConversorDivisas._obtener_tasa_conversion() + 200
        elif moneda == "COP":
            return valor

        else:
            raise ValueError("La moneda no corresponde")

        return valor * valor_convertido

    @staticmethod
    def _obtener_tasa_conversion():
        """
        Utilizamo una api que devuelve un valor min 3500 y maximo 4500
        :return: valor random entre 3500 y 4500
        """
        respuesta = requests.get("https://csrng.net/csrng/csrng.php?min=3500&max=4500")
        if respuesta.status_code == 200:
            conversion_json = respuesta.json()
            if "random" in conversion_json[0]:
                valor_api = conversion_json[0]["random"]
                return valor_api
            else:
                logging.error("La respuesta de la API no contiene el número aleatorio esperado.")
                return None
        else:
            logging.error(f"Error al obtener el número aleatorio. Código de estado: {respuesta.status_code}")
            return None