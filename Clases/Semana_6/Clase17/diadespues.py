fecha = input("Ingrese una fecha en formato dd/mm/AAAA ")
datos =fecha.split("/")
dia = int(datos[0])
mes = int(datos[1])
year = int(datos[2])
mes31 = [1,3,5,7,8,10,12]
mes30 = [4,6,9,11]
if dia<28:
    dia = dia +1
else:
    if mes in mes31:
        if dia < 31:
           dia = dia +1 
        else:
            if mes == 12:
                year = year + 1
            mes = (mes + 1) % 12
            dia = 1
    elif mes in mes30:
        if dia<30:
            dia = dia + 1
        else:
            mes = mes + 1
            dia = 1
    elif mes == 2:
        if year % 4 == 0:
            if dia < 29:
                dia = dia + 1
            else:
                mes = mes + 1
                dia = 1
        else:
            if dia < 28:
                dia = dia + 1
            else:
                mes = mes + 1
                dia = 1
            
            
print (f'El dia siguiente a {fecha} es {dia}/{mes}/{year}')
    