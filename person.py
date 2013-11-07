from node import Node

class Person(Node):

	_life_value=100
	_attack_value=0
	_defense_value=0
	_is_alive=True

	def being_attacked(self,damage):
		if(damage<0):
			damage=0
		self._life_value-=damage
		if(self._life_value<=0):
			self._life_value=0
			self._is_alive=False
