'''
print("Este programa lee tres números enteros y calcula la media ")
num1 = int(input("numero 1: ") )
num2 = int(input('Número 2: '))
num3 = int(input("Número 3: "))
media = (num1+num2+num3)/3
print(f' la media es {media}')

print("Este programa lee tres números enteros y calcula la media ")
media=0
for n in range(3):
    num = int(input(f"Ingrese el numero {n+1}: "))
    media = media + num
media = media/(n+1)
print(f' la media es {media}')


cantidad = int(input("Ingrese la cantidad de numeros a leer: "))
print(f"Este programa lee {cantidad} números enteros y calcula la media ")
media=0
for n in range(cantidad):
    num = int(input(f"Ingrese el numero {n+1}: "))
    media = media + num
media = media/(cantidad)
print(f' la media es {media}')


print('Este programa calcula la media de los numeros enteros ingresados por el usuario finaliza con 0')
listanumeros = list() # listanumeros = []
actual = -1
while actual != 0:
    actual = int(input("Ingrese un numero con 0 finaliza "))
    if actual != 0:
        listanumeros.append(actual)
media = 0
pares = list()
impares = list()
for numero in listanumeros :
    media = media + numero
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
media = media/len(listanumeros)
print(f' la media es {media}')
print("lista de pares: ", pares)
print("lista de impares ", impares)

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")

print(f"Vas por buen camino, {nombre} ({edad*12} meses).")
'''
print('Calculo de pago por trabajo')
horas = float(input('Ingrese las horas trabajadas '))
valorhora = float(input('Ingrese el valor por hora de trabajo '))
print(f'el total a pagar por trabajar {horas} horas es {horas*valorhora}')