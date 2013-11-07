class Node:

	_id=-1
	_name=""

	def get_name(self):
		return self._name

	def set_name(self,name):
		self._name=name

	def __init__(self,id):
		_id=id
		