#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from Motor import Motor


class Coche():
	
	def __init__(self,nombre):
		
		self.nombre = nombre
		self.__ruedas = None
		self.__velocimetro = None
		self.__estanque = None
		self.motor= 0.0
		self.estado = "Apagado"
		self.gasto = 0
		self.gasto_ruedas = 0
		self.tiempo = 0
		self.motor2 = 0.0
		
		
	def mover_auto(self,t):
		print ("-------------------------------------------------------------------------------")
		print ("Velocidad:", self.__velocimetro,"km/h")
		print ("Le quedan: {0:.2f} litros de gasolina a su estanque".format(self.__estanque))
		print ("va en el km: ",self.__velocimetro * t)
		print ("Sus ruedas tienen un gasto de: ",self.gasto_ruedas,"%")
		print ("Lleva ",t,"horas viajando" )
		print ("A esta velocidad su coche gasta: {0:.2f} por hora".format(self.gasto))
		print ("-------------------------------------------------------------------------------")
	
	def set_gasto_ruedas(self,gastoruedas):
		self.gasto_ruedas = self.gasto_ruedas + gastoruedas
		
	def reparar_ruedas(self,cero):
		self.gasto_ruedas = cero
		
	def get_gasto_ruedas(self):
		return self.gasto_ruedas
		
	def gasto_gasolina(self,aleatorio,velocidad):
					
		if (aleatorio == 1):
			self.gasto = (velocidad/20)
			self.__estanque = self.__estanque - self.gasto
			
		
		elif (aleatorio == 2): 
			self.gasto = (velocidad/14)
			self.__estanque = self.__estanque-self.gasto
			
	def apagar(self,estado):
		self.estado = estado
		print ("El auto se encuentra: ",self.estado)
					
	def encender(self,estado,tiempo, motor2):
		self.__estanque = (self.__estanque/100)*99
		self.estado = estado
		self.tiempo = tiempo
		a = int(input("Presione un numero para encender su auto: "))		
		print ("----------------------------------------------------------------------------")
		print ("Su auto se ha :", self.estado, "y esta listo para comenzar a moverse")
		print ("La velocidad a la que su conductor ha decidido viajar es de: ",self.__velocimetro,"km/h")
		print ("El motor de su coche es de:",motor2,"cilindradas")
		print ("Su conductor requiere",self.tiempo,"horas para llegar a su destino")
		print ("---------------------------------------------------------------------------")
		a = int(input("precione un numero para continuar: "))
		
		
	def asocia_motor(self, motor):
		if isinstance(motor,Motor):
			self.motor = motor
			
	
	def get_motor(self):
		return self.motor	
			
	def set_ruedas(self,ruedas):
		self.__ruedas = ruedas
		
	def get_ruedas(self):
		return self.__ruedas
		
	def set_velocimetro(self,velocidad):
		self.__velocimetro = velocidad
		
	def get_velocimetro(self):
		return self.__velocimetro
		
	def set_estanque(self,litros):
		self.__estanque = litros
		
	def get_estanque(self):
		return self.__estanque
				
	def mostrar_coche(self):
		print (self.motor,self.__ruedas,self.__estanque)		
			 
	
	
