"""Aquí hay una serie de varios ejercicios, que si bien no están relacionados entre sí, se colocaron
aparentando como si lo estuvieran, con el simple objetivo de que estén todas las prácticas juntas 
en un mismo archivo. 
En cada comentario se puede ver la consigna de cada ejercicio."""


#Hacer un programa para solicitar por teclado un número y luego devolver su valor elevado al cubo.
nombre = input("Por favor, ingrese su nombre: ")
print("Bienvenido", nombre + ". Como primer paso vamos a elevar al cubo el número que usted desee (debe ser un número entero). ") 
n = int(input ("Por favor, ingrese un número: "))

r = n * n * n

print("El resultado del número ingresado elevado al cubo es:", r)


#Hacer un programa que permita ingresar el año actual y el año de la fecha de nacimiento de una persona y luego calcule y emita por pantalla su edad.
print("\nPara brindarle un mejor servicio, necesitamos saber su edad. ")
aa = int(input("Por favor, ingrese el año en curso: "))
an = int(input("Ahora ingrese el año en que nació: "))

e = aa - an

print(nombre + ", su edad es:", e, "años.")


"""Hacer un programa que permita ingresar los kilómetros existentes entre dos ciudades y la velocidad promedio de un vehículo. Calcular y emitir por pantalla
el tiempo aproximado que demandará llegar de un punto a otro teniendo en cuenta los datos ingresados"""

print("\nPara acercarle promociones de su interés, necesitamos saber a qué destino le gustaría viajar.")
nombre_lugar = input("Por favor, díganos el nombre: ")

km = float(input("Por favor, indique la distancia que recorrería desde donde se encuentra, hasta llegar al destino que ingresó anteriormente (en km): "))
v = float(input("Ahora, ingrese la velocidad promedio del vehículo en el que va a realizar el viaje (en km por hora): "))

t = km * 60 / v

print("El tiempo estimado que tardará en llegar a", nombre_lugar, "es de", round(t,1), "minutos.")


"""Una casa de computación paga a sus empleados un sueldo fijo de ARS15000 más una comisión del 5% sobre el total facturado por cada empleado. Hacer un
programa para ingresar el total facturado por un empleado y que luego calcule y emita por pantalla el sueldo total a cobrar por el mismo."""

print("\nAhora", nombre +""", le vamos a ayudar a calcular el sueldo que debe pagarle a su empleado este mes, contando su sueldo fijo mensual ($15000)
y la comisión del 5% de lo que vendió este mes.""")

nombre_empleado = input("Ingrese nombre y apellido del empleado: ")
total_facturado = float(input("Ingrese el total facturado por el empleado en el mes en curso (en pesos): "))
sueldo_total = total_facturado * 0.05 + 15000

print("El sueldo que le corresponde cobrar al empleado", nombre_empleado, "es de", round(sueldo_total,2), "pesos.\n")


#Hacer un programa para ingresar por teclado las tres notas de exámenes de un alumno y luego calcule y emita por pantalla el promedio final.

print(nombre + """, sabemos que además de su emprendimiento personal también enseña. Por eso, le queremos facilitar una calculadora para que al finalizar el año lectivo,
usted pueda calcular de forma fácil el promedio de cada alumno/a.""")

nombre_alumno = input("Ingrese nombre y apellido del alumno/a: ")
examen1 = float(input("Ingrese la nota de examen del primer trimestre: "))
examen2 = float(input("Ingrese la nota de examen del segundo trimestre: "))
examen3 = float(input("Ingrese la nota de examen del tercer trimestre: "))

promedio_alumno = (examen1 + examen2 + examen3) / 3

print("El promedio del alumno/a", nombre_alumno, "es de:", round(promedio_alumno,1), "puntos.\n")



"""Una importante cadena de delivery cuenta con una promoción por tiempo limitado en la que otorga un 15% de descuento sobre el total del valor de la
compra realizada. Hacer un programa para solicitar el monto total y el mismo calcule y emita por pantalla el total a cobrar con el descuento aplicado."""

print(nombre + """, debido a que usted es un cliente muy importante para nosotros, le ofrecemos un 15% de descuento sobre el total de su compra en
FDS (Fuera de serie), una nueva hamburguesería en el barrio, cita en calle Av. Alvarez Thomas y Arizona.
Puede simular cuánto gastaría utilizando nuestra calculadora.""")

monto_total_compra = float(input("Ingrese el monto total de la compra en pesos: "))

monto_con_descuento = monto_total_compra * 0.85

print(nombre + ", el monto que deberá abonar con el 15% de descuento aplicado es de", round (monto_con_descuento,2), ("pesos. \n"))



"""Una universidad desea conocer los porcentajes de mujeres y hombres en las carreras de ciencias exactas. Se solicita un programa para cargar la cantidad de
mujeres y la cantidad de hombres y que el mismo calcule y emita por pantalla los porcentajes correspondientes."""

print("""Sabemos que en la institución donde usted enseña, precisan saber el porcentaje que asiste tanto de mujeres como de hombres.
Para ello, le facilitamos la siguiente calculadora.""")

cantidad_hombres = int(input("Por favor, ingrese la cantidad de alumnos hombres con los que cuenta la institución: "))
cantidad_mujeres =int(input("Ahora ingrese la cantidad de alumnas mujeres con las que cuenta la institución: "))

total_alumnos = cantidad_hombres + cantidad_mujeres

porcentaje_hombres = (cantidad_hombres * 100) / total_alumnos
porcentaje_mujeres = (cantidad_mujeres * 100) / total_alumnos

print("El porcentaje de alumnas de la institución es del", int(porcentaje_mujeres),"%."
      "\nEl porcentaje de alumnos es del", int(porcentaje_hombres), "%.")



"""Hacer un programa que permita ingresar por teclado dos números y que luego muestre por pantalla la suma, la resta, la multiplicación y la división de dichos
números. Se deben mostrar cuatro resultados en pantalla. Los números deben ser solicitados una única vez."""

print("\nPor último, precisamos que por favor pruebe esta calculadora, ya que es nuestro último proyecto y nos encantaría saber su opinión.")

numero1 = float(input("Por favor, ingrese un número: "))
numero2 = float(input("Por favor, ingrese el segundo número: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicación = numero1 * numero2
división = numero1 / numero2

print("El resultado de la suma es:", int(suma),
      "\nEl resultado de la resta es:", int(resta),
      "\nEl resultado de la multiplicación es:", int(multiplicación),
      "\nEl resultado de la división es:", int(división))
      
print("\n¡Muchas gracias por confiar en nosotros", nombre + "!.")

      















                               

