import requests
import os
from tabulate import tabulate
from prettytable import PrettyTable

#//Defninicion de las funciones//
def realizar_consulta(metodo, endpoint, formato, parametros):
    url = f"{endpoint}/{metodo}.{formato}?{parametros}"
    response = requests.get(url)
    return response.text

def guardar_respuesta_en_archivo(respuesta):
    escritorio = os.path.join(os.path.join(os.path.expanduser("~")), "Escritorio")
    archivo = os.path.join(escritorio, "respuesta_api.txt")
    with open(archivo, "w") as file:
        file.write(respuesta)

def mostrar_opciones_formato():
    opciones = ["json", "yaml", "xml", "csv", "xls", "xlsx"]
    opciones_str = ", ".join(opciones)
    print(f"Opciones de formato: {opciones_str}")

def mostrar_opciones_metodo():
    metodos = ["epps", "teams", "countries", "events"]  # Agrega aquí los métodos disponibles
    metodos_table = [[f"{i+1}.", metodo] for i, metodo in enumerate(metodos)]
    print("Opciones de método:")
    print(tabulate(metodos_table, headers=["Número", "Método"]))
    print()

def mostrar_parametros_epps():
    parametros = {
        "cve": "Filters by EPSS CVE ID. Multiple values are supported separated by commas. The maximum size accepted for this parameter is 2000 characters (including commas).",
        "date": "Date in the format YYYY-MM-DD (since April 14, 2021), shows the historic values for epss and percentile attributes.",
        "days": "Number of days since the EPSS score was added to the database (starting at 1, not affected by the date parameter).",
        "epss-gt": "Only display CVEs with EPSS score greater or equal than the parameter.",
        "percentile-gt": "Only display CVEs with percentile greater or equal than the parameter.",
        "epss-lt": "Only display CVEs with EPSS score lower or equal than the parameter.",
        "percentile-lt": "Only display CVEs with percentile lower or equal than the parameter.",
        "q": "Free text search at the CVE ID (allows partial matches)."
    }

    table = PrettyTable()
    table.field_names = ["Parámetro", "Tipo", "Descripción"]
    for param, description in parametros.items():
        table.add_row([param, "string", description])
    
    print("Parámetros adicionales para 'epps':")
    print(table)
    print()

def mostrar_parametros():
    parametros = {
        "fields": "Comma-separated list of fieldnames to be retrieved. Used only for limiting the available resultset.",
        "limit": "Limits the maximum number of records to be shown. Should be a number between 1 and 100.",
        "offset": "Offsets the list of records by this number. The first item is 0.",
        "sort": "Comma-separated list of fieldnames to be used to sort the resultset. Fields starting with - (minus sign) indicate a descending order. Each application should define its default sorting options.",
        "envelope": "Use true, false, 0 or 1. If set to true, it will add an object wrapping the resultset with details on the status, total records found, offset, and limit. When false, this information is returned in the response header. Defaults to true.",
        "pretty": "Use true, false, 0 or 1. Determines if the result should be pretty-printed. Defaults to false.",
        "callback": "Only for JSONP resultsets, adds the callback as a function call. Only alphanumerical characters are allowed.",
        "scope": "Collection of fieldnames to retrieve. Affects the resultset and the possible options for the parameter fields. Each data model can specify multiple available scopes."
    }
    
    table2 = PrettyTable()
    table2.field_names = ["Parámetro", "Tipo", "Descripción"]
    for param, description in parametros.items():
        table2.add_row([param, "string", description])

    print("Parámetros disponibles:")
    print(table2)
    print()
#//Main//
def main():
    endpoint = "https://api.first.org/data/v1"
    
    mostrar_opciones_metodo()
    metodo_num = int(input("Selecciona el número del método de la consulta: "))
    metodos = ["epps", "teams", "countries", "events"]  # Agrega aquí los métodos disponibles
    metodo = metodos[metodo_num - 1]
#//falta corregir este bucle, cambiarlo por un switch if/elif/esle para corregir el salto de la seleccion de mostrar opciones formato
  #añadir el parametro introducido por el usuario con epps en la url inicial//
    if metodo == "epps":
        mostrar_parametros_epps()
    else:
        mostrar_opciones_formato()
        formato = input("Ingresa el formato de la respuesta (json, yaml, xml, csv, xls, xlsx): ")

    mostrar_parametros()
    parametros = input("Ingresa los parámetros de la consulta (en el formato key1=value1&key2=value2): ")

    respuesta = realizar_consulta(metodo, endpoint, formato, parametros)
    guardar_respuesta_en_archivo(respuesta)
    print("La respuesta se ha guardado en el archivo 'respuesta_api.txt' en el escritorio.")

if __name__ == "__main__":
    main()






