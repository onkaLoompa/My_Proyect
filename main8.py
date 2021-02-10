import os.path 
import os

archivo = input("Please, enter file name: ")
 
def checkfile(archivo): 
    
    if os.path.exist(archivo):

       print("A. Read the file: ")
       print("B. Delete the file and start over: ")
       print("C: Append the file: ")
       opcion = input("Please, selec an option: ")
          if opcion == "A":
               archivoTemp = open(archivo,"r")
               archivoTemp.close()
               print(archivo)
          if opcion == "B":
               archivoTemp = open(archivo,"w")
               archivoTemp.close()
          if opcion == "C":
               archivoTemp = open(archivo,"a")
               datos = input("Please, enter data for your file: ")
               archivoTemp.write(datos)
               archivoTemp.close()

    else:

       archivoTemp = open(archivo,"w")
       datos = input("Please, enter data for your file: ")
       archivoTemp.write(datos)
       archivoTemp.close()






 