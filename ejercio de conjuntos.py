def cargarNombres (alumnos): nombre=input("Nombre: ") 
while nombre != "x":  
    alumnos.add(nombre) 
    nombre=input("Nombre: ")
    return alumnos
primaria = set()
kinder = set() 
print("ALUMNOS DE kinder")
Kinder = cargarNombres (kinder)
print("ALUMNOS DE kinder")
print("ALUMNOS DE prinaria")
primaria = cargarNombres (primaria)
print("ALUMNOS DE primaria")
primaria = cargarNombres (primaria) 
print("NOMBRES DE TODOS LOS ALUMNOS :")
for nombre in kinder | primaria:
 print (nombre)
print("NOMBRES COMUNES: ")
for nombre in kinder & primaria:
 print (nombre)

print("NOMBRES DE KINDER QUE NO SE REPITEN EN PRIMARIA: ") 
for nombreIN kinder - : primariaprint (nombre)