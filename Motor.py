#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Motor():
	
	def __init__(self, motor):		
		self.motor = motor
		
	def ensamble_motor(self):
		if (self.motor == 1):
			self.motor = 1.2
			
		elif (self.motor == 2):
			self.motor = 1.6
		
		




