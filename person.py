from node import Node

class Person(Node):

	#natural properties
	gender=1

	#character properties (color model)
	activity=1.0	#ranges in [0.0,1.0]
	control=1.0	#ranges in [0.0,1.0]
	precision=1.0	#ranges in [0.0,1.0]
	peace=1.0	#ranges in [0.0,1.0]

	#specialized properties for application
	

	_life_value=100
	_attack_value=0
	_defense_value=0
	_is_alive=True

	def __init__(self,gender):


	def being_attacked(self,damage):
		if(damage<0):
			damage=0
		self._life_value-=damage
		if(self._life_value<=0):
			self._life_value=0
			self._is_alive=False
