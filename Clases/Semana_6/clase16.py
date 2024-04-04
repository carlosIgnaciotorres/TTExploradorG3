import this

edad = 15
print(type(edad))
edad = "Veinte"
edad = 20.5
NOMBRE = "Carlos"

subtotal = 100
impuesto = 0.15
total = subtotal * (1 + impuesto)


listaCiudades = ["Tunja", "Duitama","Sogamoso","La Calera"]
listaCiudades.append("Madrid")
len(listaCiudades)
listaCiudades[5] = "Faca"

tupla = (1,2,3,4,5)
tupla.index(2)
frecuencias = (1,1,1,0,0,1,0,0,0,1,1)
frecuencias[7] = 8

numbers ={1:"one", 2:"two", 3:"tree", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eigth", 9:"nine"}
numbers.keys()
numbers.values()
numbers.get(6)
numbers[10] ="ten"
for n in numbers.keys():
    print(numbers.get(n))
print(numbers.get(6))