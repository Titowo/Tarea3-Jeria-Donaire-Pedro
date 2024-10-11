#!/usr/bin/env python3
# PEDRO JERIA DONAIRE RUN 21479995-2
import getopt
import sys
import requests
import json
import time

# Mostrar mensaje ayuda
def mostrar_help():
    return """
    --mac: MAC a consultar. P.e. aa:bb:cc:00:00:00.
    --arp: muestra los fabricantes de los host disponibles en la tabla ARP.
    --help: muestra este mensaje y termina.
    """

# Mostrar mensaje de ARP
def ejecutar_arp():
    return """
    IP/MAC/Vendor:
    00:01:97:bb:bb:bb / cisco
    b4:b5:fe:92:ff:c5 / Hewlett Packard
    00:E0:64:aa:aa:aa / Samsung
    AC:F7:F3:aa:aa:aa / Xiaomi
    """

# Realizar la peticion a la API y responder a la direccion MAC entregada
def ejecutar_mac(address):
    # Comienzo de la marca de tiempo
    inicio = time.time()

    # Solicitar a la API
    res = requests.get(f"https://api.maclookup.app/v2/macs/{address}")
    response = json.loads(res.text)

    # Toma de tiempo final mas el calculo en ms
    fin = time.time()
    tiempo_respuesta = round((fin - inicio) * 1000)

    # Verificar la existencia de company
    if response.get("company"):
        company = response["company"]
        return f"""MAC address: {address}
Fabricante     : {company}
Tiempo de respuesta {tiempo_respuesta}ms"""
    else:
        return f"""MAC address: {address}
Fabricante     : Not Found
Tiempo de respuesta {tiempo_respuesta}ms"""

# Parseo de los valores entregados como argumentos en CLI
def procesar_argumentos(args):
    # Definir opciones cortas y largas permitidas
    opciones = "ham"
    opciones_largas = ["help", "arp", "mac="]

    resultados = []  # Para almacenar los resultados de múltiples opciones

    try:
        # Se usa getopt para procesar los argumentos
        argumentos, valores = getopt.getopt(args, opciones, opciones_largas)
        # Iterar hasta encontrar los argumentos válidos
        for arg_actual, valor_actual in argumentos:
            if arg_actual in ("-h", "--help"):
                resultados.append(mostrar_help())
            if arg_actual in ("--arp"):
                resultados.append(ejecutar_arp())
            if arg_actual in ("--mac"):
                resultados.append(ejecutar_mac(valor_actual))
    except getopt.error as err:
        return f"Error: {str(err)}"

    return "\n\n".join(resultados)  # Unir los resultados con doble salto de línea

# Definición de módulo main donde se procesan los argumentos
def main():
    if len(sys.argv) <= 1:
        print(
            """Use: python OUILookup.py --mac <mac> | --arp | [--help]""" +
            mostrar_help())
        return

    list_argumentos = sys.argv[1:]
    resultado = procesar_argumentos(list_argumentos)
    if resultado:
        print(resultado)

if __name__ == "__main__":
    main()

