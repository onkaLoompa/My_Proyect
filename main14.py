##
# Siete
##

# _*_ coding: utf-8 _*_


from random import shuffle

def crearMesa():
    Mesa = []

    piezas = ['S', 'C', 'R']   # 'S' = Sota, 'C' = Caballo, 'R' = Rey
    for i in range(3):
        for carta in range(1,8):   #Cartas del 1 al 7
            Mesa.append(str(carta))

        for carta in piezas:
            Mesa.append(carta)
    return Mesa
mesaCartas = crearMesa()
shuffle(mesaCartas)
print(mesaCartas)

class Jugador:
    def __init__(self,mano = [], dinero = 100):
      self.mano = mano
      self.puntos = self.setPuntos()
      self.dinero = dinero
      self.apuesta = 0


    def __str__(self):
        manoActual = " "
        for carta in self.mano:
            manoActual += str(carta + " ")

        estatusFinal = manoActual + "puntos " + str(self.puntos)
        return estatusFinal

    def setPuntos(self):
        self.puntos = 0
        #print(self.puntos)

        DiccCartasPiezas = {"S":1,"C":1,"R":1,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7}

        for carta in self.mano:
            self.puntos += DiccCartasPiezas[carta]
            if self.puntos > 7:
                self.puntos -= 5


    def hit(self, carta):
        self.mano.append(carta)
        self.puntos = self.setPuntos()

    def play(self, nuevaMano):
        self.mano = nuevaMano
        self.puntos = self.setPuntos()

    def apuestaDinero(self, cantidad):
        self.dinero -= cantidad
        self.apuesta += cantidad

    def ganador(self, resultado):
        if resultado == True:
            self.puntos = 7
            self.dinero += 2*self.apuesta
            self.apuesta = 0
        else:
            self.apuesta = 0

    def empate(self):
        self.dinero += self.apuesta
        self.apuesta = 0

def printBanca(banca):
    for carta in range(len(banca.mano)):
        if carta == 0:
            print("X",end=" ")
        elif carta == len(banca.mano) -1:
            print (banca.mano[carta])
        else:
            print(banca.mano[carta], end=" ")

mesaCartas = crearMesa()

primeraMano = [mesaCartas.pop()]

segundaMano = [mesaCartas.pop()]

Jugador1 = Jugador(primeraMano)

Banca = Jugador(segundaMano)

mesaCartas = crearMesa()

while(True):
    if len(mesaCartas) < 20:
        mesaCartas = crearMesa()

    primeraMano = [mesaCartas.pop()]
    segundaMano = [mesaCartas.pop()]

    Jugador1.play(primeraMano)
    Banca.play(segundaMano)

    apuesta = int(input("¿Cuanto apuestas?: "))

    print(mesaCartas)
    Jugador1.apuestaDinero(apuesta)
    #printBanca(Banca)
    print(Jugador1)

    while(Jugador1.puntos < 7):
        accion = input("¿Quieres otra carta?(s/n): ")
        if accion == "s":
            Jugador1.hit(mesaCartas.pop())
            print(Jugador1)
            printBanca(Banca)
        else:
            break

    while Banca.puntos < 5:
        print(Banca)
        Banca.hit(mesaCartas.pop())

    if Jugador1.puntos > 7:
        if Banca.puntos > 7:
            Jugador1.empate()
        else:
            Jugador1.ganador(False)
    elif Jugador1.puntos > Banca.puntos:
        Jugador1.ganador(True)
    elif Jugador1.puntos == Banca.puntos:
        Jugador1.empate()
    else:
        if Banca.puntos > 7:
            Jugador1.ganador(True)
        else:
            Jugador1.ganador(False)

    print(Jugador1.dinero)
    print(Banca)





