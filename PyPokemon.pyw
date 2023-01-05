from moduloPokemon import *
from tkinter import *
from random import randint
import pickle

#----Creacion de la ventana principal, icono, etc
root = Tk()
root.title("PyPokemon")
root.iconbitmap("./source/pokeball.ico")
root.geometry("800x500")

root.resizable(False, False)
#-----------------------------------------------

#----Se establecen algunas variables, colores, imagenes, y recursos que seran utilizados en el juego-----------
fuente = "Comic Sans Ms"
cesped = "#aaffaa"
buttonColor = "#EBEDEF"
redColor = "#E74C3C"
blue = "#2980B9"


pokes = [
["Bulbasaur", PhotoImage(file = "./source/bulbasaur.png").subsample(2), ["Placaje", "Gruñido", "Latigo cepa"], "Planta"],
["Charmander", PhotoImage(file = "./source/charmander.png").subsample(2), ["Arañazo", "Gruñido", "Ascuas"], "Fuego"],
["Squirtle", PhotoImage(file = "./source/squirtle.png").subsample(2), ["Placaje", "Latigo", "Pistola agua"], "Agua"]
]
selection = 0
miPokemon = 0
Jugador = ""
Rival = ""
rivalPokemon = 1
dialogoParaText = []
indexDialogo = 0
inicio = True
end = False #Controla fin de un turno
fin = False #Controla fin de la partida

#-Eventos dentro de la pelea(control): 0.- Mostrar opciones del jugador y ataque, 1.- Ataque rival
eventos = 0

root.config(bg = "#aaaaff")
#----------------------------------------------------------------------------------------------------

#---Funciones adicionales---------------------------

def textoDialog(texto = dialogoParaText):
	'''
	Se encarga de mostrar los dialogos, y al ser uno de los botones mas importantes,
	controla tambien los eventos
	'''
	global inicio
	global indexDialogo
	global textoDialogo
	global eventos
	global end
	global fin

	if (inicio): root.config(bg = "#aaaaff")

	if (indexDialogo < len(texto)):
		textoDialogo.config(text = texto[indexDialogo])
		indexDialogo = indexDialogo + 1
	elif (inicio):
		dialogoParaText = []
		indexDialogo = 0
		dialogo.pack_forget()
		batalla.pack(side = "top")
		cambioSubMenu("ataques")
		root.config(bg = cesped)
		inicio = False
	elif (end and comprobar()):
		dialogoParaText = []
		indexDialogo = 0
		dialogo.pack_forget()
		Ataques.pack(fill = "x", side = "bottom")
		cambioSubMenu("ataques")
		end = False
	elif (comprobar()):
		dialogoParaText = []
		indexDialogo = 0
		Eventos()
	elif (not comprobar() and fin):
		root.destroy()


		


def cambioSubMenu(destino):
	global indexDialogo
	global dialogoParaText

	if (destino == "dialogo"):
		indexDialogo = 0
		dialogo.pack(side = "bottom", fill = "x")


	elif (destino == "ataques"):
		Ataques.pack(side = "bottom", fill = "x")

#---------------------------------------------------


#---Interfaz de Inicio------------------------------------------------------------------------------
#En esta parte del codigo se genera la interfaz de la seleccion del pokemon y acciones de los botones

def changeButton(direccion):
	global selection
	global pokes

	if (selection < 2 and direccion == "right"):
		selection += 1
	elif direccion == "right":
		selection = 0

	if (selection > 0 and direccion == "left"):
		selection -= 1
	elif direccion == "left":
		selection = 2

	pokeSelectionText.config(text = pokes[selection][0])
	pokeSelectionImg.config(image = pokes[selection][1])
	pokeSelectionButton.config(text = f"¿Eliges a {pokes[selection][0]}?")

def select(pokemon):
	global dialogo
	global miPokemon
	global rivalPokemon
	global dialogoParaText
	global JugadorImage
	global Jugador
	global Rival

	miPokemon = pokemon

	while True:
		rivalPokemon = randint(0,2)
		if (rivalPokemon != miPokemon):
			break

	dialogoParaText = []
	dialogoParaText.extend([f"Has Selegido a {pokes[miPokemon][0]}", f"El rival ha Escogido a {pokes[rivalPokemon][0]}"])

	seleccion.pack_forget()
	cambioSubMenu("dialogo")

	Jugador = Pokemon(pokes[miPokemon][0], pokes[miPokemon][3], pokes[rivalPokemon][3])
	Rival = Pokemon(pokes[rivalPokemon][0], pokes[rivalPokemon][3], pokes[miPokemon][3])

	JugadorImage.config(image = pokes[pokemon][1])
	RivalImage.config(image =pokes[rivalPokemon][1])

	TextQue.config(text = f"¿Que deberia hacer {Jugador.nombre}?")
	Ataque1.config(text = pokes[pokemon][2][0])
	Ataque2.config(text = pokes[pokemon][2][1])
	Ataque3.config(text = pokes[pokemon][2][2])

	textoDialog(dialogoParaText)


seleccion = Frame(root, background = cesped, width = 800)

Label(seleccion, text = "Selecciona a tu Pokemon", font = (fuente, 14, ""), justify = "center", width = 73, height = 2, bg = redColor, fg = "white").grid(row=0, column=0, columnspan = 3)

pokeSelectionImg=Label(seleccion, image = pokes[selection][1], bg = cesped)
pokeSelectionImg.grid(row = 1, column = 1, padx = 10, pady = 10)

pokeSelectionText = Label(seleccion, text = "Bulbasaur", justify = "center", font = (fuente, 16, ""), height = 2, bg = cesped)
pokeSelectionText.grid(row=2, column = 1, pady = 15)

Button(seleccion, text = " < ", width = 20, height = 1, font = ("",10, "bold"), command = lambda:changeButton("left"), bg = buttonColor).grid(row = 2, column = 0, pady=10, sticky = "e")
Button(seleccion, text = " > ", width = 20, height = 1, font = ("",10, "bold"), command = lambda:changeButton("right"), bg = buttonColor).grid(row = 2, column = 2, pady=10, sticky = "w")

pokeSelectionButton = Button(seleccion, text = f"¿Eliges a {pokes[selection][0]}?", width = 25, bg = redColor, fg = "white", font = (fuente,13, ""), command = lambda:select(selection))
pokeSelectionButton.grid(row = 3, column = 0, columnspan = 3)

Dinero = Label(seleccion, text = "$", height = 1, width = 50, bg = buttonColor, font = (fuente, 12, ""))
Dinero.grid(row=4, column=0, columnspan = 3, pady=15)

seleccion.pack(fill = "both", expand = "True")
#------------------------------------------------------------------------------------------------------

#----Ventana de Dialogo--------------------------------------------------------------------------------

dialogo = Frame(root, bg = blue)
textoDialogo = Label(dialogo, text = "", width = 66, height = 2, font = (fuente, 12, ""))
textoDialogo.grid(row = 0, column = 0, padx = 10, pady = 10)
Button(dialogo, text = "Siguiente", bg = redColor, fg = "white", height = 2, font = (fuente, 12, ""), command = lambda:textoDialog(dialogoParaText)).grid(row = 0, column = 1, padx = 10, pady = 10)


#------------------------------------------------------------------------------------------------------



#----Batalla Interfaz----------------------------------------------------------------------------------

batalla = Frame(root, bg = cesped)
JugadorImage = Label(batalla, image = pokes[miPokemon][1], bg = cesped)
JugadorImage.grid(row=0, column = 0, sticky = "w", padx = 10, pady = 50)

RivalImage = Label(batalla, image = pokes[rivalPokemon][1], bg = cesped)
RivalImage.grid(row=0, column = 3, sticky = "e", padx = 10, pady = 50)

VidaJugador = Label(batalla, text = "HP: 100", width = 10, bg = "#D5F5E3", fg = "black", font = (fuente, 12, ""))
VidaJugador.grid(row=0, column=1, padx=10, pady=40, sticky="sw")

VidaRival = Label(batalla, text = "HP: 100", width = 10, bg = "#D5F5E3", fg = "black", font = (fuente, 12, ""))
VidaRival.grid(row=0, column=2, padx=10, pady=40, sticky="ne")


#----Botones de ataque---------------------------------------------------------------------------

Ataques = Frame(root)
Ataques.config(bg = blue)

TextQue = Label(Ataques, text = "¿Que deberia hacer?", width = 60, font = (fuente, 12, ""))
TextQue.grid(row=0, column=0, columnspan=3, padx=15, pady = 10)

Ataque1 = Button(Ataques, text = "ataque1", font = (fuente, 12, ""), width = 23, command=lambda:Eventos(pokes[miPokemon][2][0]))
Ataque1.grid(row=1, column=0, padx = 15, pady = 10)

Ataque2 = Button(Ataques, text = "ataque2", font = (fuente, 12, ""), width = 22, command=lambda:Eventos(pokes[miPokemon][2][1]))
Ataque2.grid(row=1, column=1, padx = 15, pady = 10)

Ataque3 = Button(Ataques, text = "ataque1", font = (fuente, 12, ""), width = 23, command=lambda:Eventos(pokes[miPokemon][2][2]))
Ataque3.grid(row=1, column=2, padx = 15, pady = 10)

#------------------------------------------------------------------------------------------------

#-----Funcion eventos----------------------------------------------------------------------------

def Eventos(ataque=""):
	'''
	Funcion que controla los ataques de los pokemon segun el evento en curso
	'''

	global eventos
	global dialogoParaText
	dialogoParaText = []
	indexDialogo = 0
	global end
	global fin

	if (ataque != "" and comprobar()):
		if (randint(1,5) == 3): ataque = "fallo"
		dialogoParaText.extend(Jugador.atacar(ataque, Rival))
		Ataques.pack_forget()
		if (not comprobar()): dialogoFinal()
		textoDialog(dialogoParaText)
		dialogo.pack(side = "bottom", fill = "x")

	elif ataque == "" and Rival.vida > 0 and end != True and comprobar():
		ataqueriv = randint(1,10)
		if ataqueriv > 0 and ataqueriv <=3: atacar = pokes[rivalPokemon][2][0]
		if ataqueriv > 3 and ataqueriv <=5: atacar = pokes[rivalPokemon][2][1]
		if ataqueriv > 5 and ataqueriv <=8: atacar = pokes[rivalPokemon][2][2]
		if ataqueriv > 8 and ataqueriv <=10: atacar = "fallo"
		
		dialogoParaText.extend(Rival.atacar(atacar, Jugador))
		if (not comprobar()): dialogoFinal()
		textoDialog(dialogoParaText)

		end = True

	if (Jugador.vida > 0):
		VidaJugador.config(text = f"HP: {round(Jugador.vida, 1)}")
	if (Rival.vida > 0):
		VidaRival.config(text = f"HP: {round(Rival.vida,1)}")


def comprobar():
	global fin
	if (Jugador.conVida() and Rival.conVida()): return True
	else: return False

def dialogoFinal():
	global fin
	global dinero
	cambioDinero = randint(100,300)

	if (Rival.vida == 0):
		RivalImage.destroy()
		VidaRival.destroy()
		textoDialogo.config(fg = "green")
		dialogoParaText.extend([f"{Rival.nombre} se ha debilitado", f"Has ganado $({cambioDinero})"])
		dinero = dinero + cambioDinero

	if (Jugador.vida == 0):
		JugadorImage.destroy()
		VidaJugador.destroy()
		textoDialogo.config(fg = "red")
		dialogoParaText.extend([f"{Jugador.nombre} se ha debilitado", f"Has perdido $({cambioDinero})"])
		dinero = dinero - cambioDinero


	file = open("datos", "wb")
	pickle.dump(dinero, file)
	file.close()

	fin = True

	
#----Cargar Dinero-----------------------------------------------

try:
	file = open("datos", "rb")
	dinero = pickle.load(file)
	file.close()
except:
	dinero = 0

Dinero.config(text = f"${dinero}")


root.mainloop()
