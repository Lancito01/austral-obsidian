"""
Ejercicios de Python en clase
"""

# ? Actividad 1
num1 = 1
num2 = 2
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

# ? Actividad 2
name = "Andrés"
year_dob = 2004
print("Me llamo", name, "y nací en", year_dob)

# ? Actividad 3
amount_of_students = 42
students_per_group = 3
print("Cantidad de grupos completos:", amount_of_students // students_per_group)
print("Cantidad de alumnos sin grupo:", amount_of_students % students_per_group)

# ? Actividad 4 (Extra)
print("Número de 3 cifras:", num3 := input("Ingresar un número de 3 cifras: "))
print("Centenas:", num3[0])
print("Decenas:", num3[1])
print("Unidad:", num3[2])
