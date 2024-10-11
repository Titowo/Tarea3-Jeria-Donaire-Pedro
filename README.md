# OUILookup Tool

### Integrante Pedro Jose Jeria Donaire - Pedro.jose@alumnos.uv.cl

Esta herramienta permite realizar consultas sobre direcciones MAC y mostrar información de la tabla ARP de dispositivos locales o de la red. Utiliza una API externa para consultar el fabricante de una dirección MAC específica.

## Características

- **Consulta de dirección MAC**: Ingresa una dirección MAC y obtén información sobre el fabricante.
- **Tabla ARP**: Muestra los fabricantes de los dispositivos disponibles en la tabla ARP.
- **Ayuda**: Muestra las opciones de uso del programa.

## Requisitos

- **Python 3.x**
- Dependencias externas:
  - `requests`: Para hacer solicitudes HTTP. Puedes instalarla usando el siguiente comando:
    ```bash
    pip install requests
    ```

## Uso

Puedes ejecutar el script con diferentes opciones de la línea de comandos.

### Opciones

- `--mac <direccion_mac>`: Consulta el fabricante asociado a una dirección MAC.
- `--arp`: Muestra la tabla ARP con los fabricantes de dispositivos detectados.
- `--help`: Muestra el mensaje de ayuda.

### Ejemplos de uso

1. **Consulta de una dirección MAC específica**:
    ```bash
    python OUILookup.py --mac aa:bb:cc:00:00:00
    ```

2. **Mostrar la tabla ARP**:
    ```bash
    python OUILookup.py --arp
    ```

3. **Mostrar el mensaje de ayuda**:
    ```bash
    python OUILookup.py --help
    ```

4. **Ejecutar múltiples comandos al mismo tiempo**:
    ```bash
    python OUILookup.py --mac aa:bb:cc:00:00:00 --arp
    ```

## Detalles Técnicos

- **MAC Lookup API**: El programa utiliza la API de [maclookup.app](https://maclookup.app) para obtener la información del fabricante de una dirección MAC.
  
- **Multicomandos**: Este script permite la ejecución de múltiples argumentos en la misma llamada. Por ejemplo, puedes consultar una dirección MAC y mostrar la tabla ARP al mismo tiempo.
