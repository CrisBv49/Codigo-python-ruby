import re

opcion = 0

def procesar_opcion(textfile, regex):
    diccionario = {}
    reg = re.compile(regex) 
    for line in textfile:
        lista = reg.findall(line) 
        for elemento in lista:
            re.search(regex, elemento)
            diccionario[elemento]= diccionario.get(elemento,0)+1
    textfile.close()
    imprimir_diccionario(diccionario)

def imprimir_diccionario (diccionario):
    total = sum(diccionario.values())
    print(f"\nCoincidencias : {total}\n")
    for identificador, cantidad in diccionario.items():
        print(f"{identificador}: {cantidad} veces")

while opcion != 21:
    print (""" 
           \033[1;34m1-Buscar Palabras Reservadas
           2-Identificadores o Variables que inicien con mayúscula
           3-Identificadores que inicien con Mayúscula cuya longitud sea mayor a 7
           4-Los identificadores o variables que contengan algún guión bajo
           5-Identificadores o variables que finalicen con un número
           6-Identificadores o variables que inician con alguna vocal
           7-Expresiones que permitan asignar un valor a una variable, ejemplo:a = 1,pi = 3.14159 modificar
           8-Expresiones aritméticas básicas, ejemplo: cont + 1, suma =a - b
           9-Expresiones aritméticas que contengan el operador módulo
           10-Expresiones encerradas entre comillas
           11-Comentarios
           12-Expresiones condicionales, ejemplo: num1 <>num2, edad>= 18
           13-Expresiones lógicas con el operador and, ejemplo: num1 > 1 and num3 <= 18
           14-Expresiones lógicas con el operador or, ejemplo: edad> 18 or edo_civil <='casado
           15-Encabezado de las estructura de control if/while/for
           16-Arreglos
           17-Funciones o métodos
           18-Clases
           19-Correos electrónicos
           20-Url's
           21-Salir\033[0m
           """)
    opcion = int(input(f"\033[1;{33}m SELECCIONE UNA OPCION \033[0m"))
    
    print(f"\033[1;{35}m")
    if opcion == 1:
        archivo = "ruby.txt" 
        textfile = open(archivo, "r") 
        regex = r'\b(' + 'BEGIN|END|alias|and|begin|break|case|class|def|defined?|do|else|elsif|end|ensure|false|for|if|in|module|next|nil|not|or|redo|rescue|retry|return|self|super|then|true|undef|unless|until|when|while|yield' + r')\b'
        procesar_opcion(textfile, regex)
    elif opcion == 2:
        archivo = "ruby.txt"
        textfile = open(archivo, "r")
        regex = r'\b[A-Z][a-zA-Z_0-9]*\b'
        procesar_opcion(textfile, regex)   
    elif opcion == 3:
        archivo = "ruby.txt"
        textfile = open(archivo, "r")
        regex = r'\b[A-Z][a-zA-Z_0-9]{7,}\b'
        procesar_opcion(textfile, regex)
    elif opcion == 4:
        archivo = "ruby.txt"
        textfile = open(archivo, "r")
        regex = r'\b[a-zA-Z_0-9]*_[a-zA-Z_0-9]*\b'
        procesar_opcion(textfile, regex)
    elif opcion == 5:
        archivo = "ruby.txt"
        textfile = open(archivo, "r")
        regex = r'\b[a-zA-Z_0-9]*[0-9]\b'
        procesar_opcion(textfile, regex)
    elif opcion == 6:
        archivo = "ruby.txt"
        textfile = open(archivo, "r")
        regex = r'\b[aeiouAEIOU][a-zA-Z_0-9]*\b'
        procesar_opcion(textfile, regex)
    elif opcion == 7:
     def procesar_opcion(archivo, regex):
        for linea in archivo:
         match = re.search(regex, linea)
         if match:
             print(f"Busqueda: {match.group(0)}")
     archivo = "ruby.txt"
     with open(archivo, "r") as textfile:
            regex = r'\b([a-zA-Z_][a-zA-Z_0-9]*)\s*=\s*([^;]*)'    
            procesar_opcion(textfile, regex)
    elif opcion == 8:
        archivo = "ruby.txt"
        textfile = open(archivo, "r")
        regex = r'\b\w+\s*=\s*\w+\s*[\+\-\*\/]\s*\w+\b'
        procesar_opcion(textfile, regex)
    elif opcion == 9:
        archivo = "ruby.txt"
        textfile = open(archivo, "r")
        regex = r'\b\d+\s*%\s*\d+\b|\b[a-zA-Z_][a-zA-Z_0-9]*\s*%\s*\d+\b|\b\d+\s*%\s*[a-zA-Z_][a-zA-Z_0-9]*\b|\b[a-zA-Z_][a-zA-Z_0-9]*\s*%\s*[a-zA-Z_][a-zA-Z_0-9]*\b'
        procesar_opcion(textfile, regex)
    elif opcion == 10:
        archivo = "ruby.txt"
        textfile = open(archivo, "r")
        regex = r'(["\'])(.*?)(\1)'
        procesar_opcion(textfile, regex)
    elif opcion == 11:
        archivo = "ruby.txt"
        textfile = open(archivo, "r")
        regex = r'#.*'
        procesar_opcion(textfile, regex)
    elif opcion == 12:
        archivo = "ruby.txt"
        textfile = open(archivo, "r")
        regex = r'\b[a-zA-Z_][a-zA-Z_0-9]*\s*(==|!=|<>|<=|>=|<|>)\s*[a-zA-Z_0-9]+\b'
        procesar_opcion(textfile, regex)
    elif opcion == 13:
     def procesar_opcion(archivo, regex):
        for linea in archivo:
         match = re.search(regex, linea)
         if match:
             print(f"Busqueda: {match.group(0)}")
     archivo = "ruby.txt"
     with open(archivo, "r") as textfile:
            regex = r'(\w+)\s*([><=!]+)\s*(\w+)\s*&&\s*(\w+)\s*([><=!]+)\s*(\w+)'
            procesar_opcion(textfile, regex)
    elif opcion == 14:
     def procesar_opcion(archivo, regex):
        for linea in archivo:
         match = re.search(regex, linea)
         if match:
             print(f"Busqueda: {match.group(0)}")
     archivo = "ruby.txt"
     with open(archivo, "r") as textfile:
            regex = r'(\w+)\s*([><=!]+)\s*(\w+)\s*(\|\||or)\s*(\w+)\s*([><=!]+)\s*(\w+)'
            procesar_opcion(textfile, regex)
    elif opcion==15:
     def procesar_opcion(archivo, regex):
        for linea in archivo:
         match = re.search(regex, linea)
         if match:
             print(f"Busqueda: {match.group(0)}")
     archivo = "ruby.txt"
     with open(archivo, "r") as textfile:
            regex = r'\b(if|while|for)\b\s*\(?.*?\)?\s*(do|then)?'
            procesar_opcion(textfile, regex)
    elif opcion == 16:
        archivo = "ruby.txt" 
        textfile = open(archivo, "r") 
        regex = r'\b[a-zA-Z_][a-zA-Z_0-9]*\s*=\s*\[.*?\]'
        procesar_opcion(textfile, regex)
    elif opcion ==17:
        archivo = "ruby.txt"
        textfile = open(archivo, "r")
        regex = r'\bdef\s+[a-zA-Z_][a-zA-Z_0-9]*\s*(\([a-zA-Z_0-9,\s]*\))?\s*'
        procesar_opcion(textfile, regex)
    elif opcion ==18:
        archivo = "ruby.txt"
        textfile = open(archivo, "r")
        regex = r'\bclass\s+[a-zA-Z_][a-zA-Z_0-9]*\s*'
        procesar_opcion(textfile, regex)
    elif opcion == 19:
        archivo = "ruby.txt"
        textfile = open(archivo, "r") 
        regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        procesar_opcion(textfile, regex)
    elif opcion == 20:
        archivo = "ruby.txt" 
        textfile = open(archivo, "r") 
        regex = r'https?://[a-zA-Z0-9.-]+(?:/[^\s]*)?'
        procesar_opcion(textfile, regex)
    