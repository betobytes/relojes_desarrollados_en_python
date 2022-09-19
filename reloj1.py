#importamos las librerias que le bridaran el aspecto 
from tkinter import *
from time import strftime
#generamos la ventana  y sus propiedades
ventana = Tk()
ventana.title("reloj")
tamano = 32
#creamos la funcion time que posee el reloj
def time():
	string = strftime(" [ %H : %M : %S  %p ]")
	label.config(text = string)
	label.after(1000, time)
#le damos caracteristicas a la ventana
 
label  = Label(ventana, font=("ds-digital", tamano), background= "limegreen", foreground="black" )
label.pack(anchor = "center")
#iniciamos el reloj 
time()
#lo mantenemos funcionando en un bucle
mainloop()
