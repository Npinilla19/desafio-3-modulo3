import sys 
ventas = {
    "Enero": 15000, "Febrero": 22000, "Marzo": 12000, "Abril": 17000, "Mayo": 81000, "Junio": 13000, "Julio": 21000, "Agosto": 41200, "Septiembre": 25000, 
    "Octubre": 21500, "Noviembre": 91000, "Diciembre": 21000,
}

if len(sys.argv) != 2:  
    print("Por favor, ingrese un umbral como argumento en la línea de comandos.")  
    sys.exit(1)  

try:  
    umbral = int(sys.argv[1])   
    resultado = {mes: venta for mes, venta in ventas.items() if venta > umbral}   
    print(resultado)  

except ValueError:  
    print("Por favor, ingrese un número entero válido como argumento.")
