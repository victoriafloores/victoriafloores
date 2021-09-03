lista_articulos = list()
def agregar_articulos():
 print()
print("Favor de agregar tus artículos que selecciono")
print()
articulos = input("Agrega tus artículo que va a comprar: ")
#Utilizamos string.capitaliza() para convertir nuestra primera letra en mayuscula
lista_articulos.append(articulos.capitalize())
print("Articulo agregados")
print()

def borrar_articulos():
 articulo = input("Elementos a eliminar: ")
#Agregamos de nuevo string.capitaliza()para que python no marque error
lista_articulos.remove(articulos.capitalize())
print("El articulo se ha borrado con exito!")
#Funcion para imprimir los artculos de nuestra lista
def ver_lista():

#print(lista_articulos)
 print()
print("Articulos en su lista")
print("uste va a comprar algo")
for articulos in lista_articulos:
 print("que desea llevar ")
print(articulos)
print("usted pago con un billete")
print("desea rendodear")
print("Estos son tus artículos seleccionados")
print()
whiletrue: 
tryelse:
print ("no es una opcion correcta") 
if opcion < 0 or opcion >4:
  
  agregar_articulos()
if opcion == 1:
 borrar_articulos()

elif opcion == 3:
 ver_lista()
elif opcion == 2:
else:
 break
print("Menú")
print ("1.- Salir")
print ("2.- Borrar artículos")
print ("3.- Ver lista de artículos")
print ("4.- Agregar artículos")
opcion = int(input("usted que deseas hacer: "))
except ValueError:
print("Favor de ingresar una opcion correcta")
