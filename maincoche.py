#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from Coche import Coche
from Motor import Motor
from random import randint, uniform , random

distancia = 0
tiempo = randint(1,10)
aleatorio =  randint(1,2)
velocidad = randint(30,120)

#ensamble del coche
motor = Motor(aleatorio)
coche = Coche("coche")
coche.asocia_motor(motor)
motor.ensamble_motor()

motor2 = format(motor.motor)

coche.set_ruedas(4)
coche.set_estanque(32)
coche.set_velocimetro(velocidad)

coche.encender("encendido",tiempo , motor2)
t=1
while (t<tiempo+1):
	
	coche.gasto_gasolina(aleatorio,velocidad)
	gastoruedas = randint(1,10)
	coche.set_gasto_ruedas(gastoruedas)
	
	if (0 < coche.get_estanque()):
		if (coche.get_gasto_ruedas() < 90 ):
			coche.mover_auto(t)
			
		else:
			print ("----------------------------------------------------------")
			print ("Sus ruedas tienen un daño mayor a 90 % ")
			print ("El conductor ha tenido que detener el auto para evitar un accidente")
			print ("el conductor tendra que cambiar las ruedas")
			print ("demorara 1 hora en arreglarla por lo que tardara 1 hora mas en llegar a su destino")
			print ("---------------------------------------------------------")
			tiempo = tiempo + 1
			coche.reparar_ruedas(0)
			
	else:
		print ("----------------------------------------")
		print ("su coche se ha quedado sin gasolina ")
		print ("el ultimo lugar en el cual fue visto es el km: ",coche.get_velocimetro()*(t-1))
		print ("------------------------------------------")
		break
		
	opcion = int(input("presione cualquier numero para continuar: "))
	t = t+1


if (t==tiempo+1):
	print ("")
	print ("El conductor llego a su destino luego de un largo viaje")
	coche.apagar("apagado")
	print ("")
