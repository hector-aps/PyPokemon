from random import randint

class Pokemon():
	def __init__(self, nombre, tipo, tipoRival):

		'''
		Funcion constructora de pokemon, recibe por parametros: nombre, tipo y tipo de rival.
		'''

		self.nombre = nombre
		self.vida = 100
		self.tipo = tipo
		self.ataque = 1
		self.defensa = 1
		self.tipoRival = tipoRival

		#Establecer ataques de los pokemon
		self.ataques = {
		"Placaje": ["normal", 15],
		"Arañazo": ["normal", 15],
		"Latigo cepa": ["esp", 8, 30],
		"Ascuas": ["esp", 8, 30],
		"Pistola agua": ["esp", 8, 30],
		"Gruñido": ["bajaAtaque"],
		"Latigo": ["bajaDefensa"]}

		#Verificar si los ataques de tipo son efectivos
		if (self.tipo == "Fuego" and tipoRival == "Planta"): self.efectividad = True
		elif (self.tipo == "Planta" and tipoRival == "Agua"): self.efectividad = True
		elif (self.tipo == "Agua" and tipoRival == "Fuego"): self.efectividad = True
		else: self.efectividad = False


	def atacar(self, ataque, rival):
		'''
		Funcion encargada de efectuar los ataques realizados por los pokemon, adicionalmente regresa
		un dialogo que se mostrara en el juego para dar contexto al jugador, recibe: ataque, rival
		'''
		try:
			if (self.ataques[ataque][0] == "normal"): # En caso de ataque tipo normal
				aleatorio = randint(1,5) #Posibilidad de ataque critico: 20%
				if aleatorio == 3:
					daño = self.ataques[ataque][1] * (0.4 + self.ataque) / rival.defensa
					rival.vida = rival.vida - daño
					if (rival.vida < 0): rival.vida = 0
					return [f"{self.nombre} ha usado {ataque}, ataque critico (-{round(daño,1)})"]
				else:
					daño = self.ataques[ataque][1] * self.ataque / rival.defensa
					rival.vida = rival.vida - daño
					if (rival.vida < 0): rival.vida = 0
					return [f"{self.nombre} ha usado {ataque} (-{round(daño,1)})"]

			if (self.ataques[ataque][0] == "esp"): # En caso de ataque del tipo del pokemon
				if (self.efectividad == True): #Verificar si el ataque es efectivo
					atack = 2
					mens = "Es muy efectivo."
				else:
					atack = 1
					mens = "No es muy efectivo."

				aleatorio = randint(1,5) #Posibilidad de ataque critico: 20%
				if aleatorio == 3:
					daño = self.ataques[ataque][atack] * (0.4 + self.ataque) / rival.defensa
					rival.vida = rival.vida - daño
					if (rival.vida < 0): rival.vida = 0
					return [f"{self.nombre} ha usado {ataque}, ataque critico (-{round(daño,1)})", mens]
				else:
					daño = self.ataques[ataque][atack] * self.ataque / rival.defensa
					rival.vida = rival.vida - daño
					if (rival.vida < 0): rival.vida = 0
					return [f"{self.nombre} ha usado {ataque} (-{round(daño,1)})", mens]


			if (self.ataques[ataque][0] == "bajaDefensa"):
				if (rival.defensa > 0.6):
					rival.defensa = rival.defensa - 0.2
					return [f"{self.nombre} ha usado {ataque}", f"La defensa de {rival.nombre} ha bajado!"]
				else:
					return [f"{self.nombre} ha usado {ataque}", f"La defensa de {rival.nombre} no puede bajar mas."]

			if (self.ataques[ataque][0] == "bajaAtaque"):
				if (rival.ataque > 0.6):
					rival.ataque = rival.ataque - 0.2
					return [f"{self.nombre} ha usado {ataque}", f"El ataque de {rival.nombre} ha bajado!"]
				else:
					return [f"{self.nombre} ha usado {ataque}", f"El ataque de {rival.nombre} no puede bajar mas."]
		except: pass
		if (ataque == "fallo"):
			return [f"{self.nombre} ha atacado, pero fallo!"]

	def conVida(self):
		'''
		Funcion que se encarga de verificar si el pokemon sigue con vida
		'''
		if (self.vida > 0): return True
		else: return False
