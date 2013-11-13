class Node:

	_next_id=1

	_id=-1
	_name=""

	def get_name(self):
		return self._name

	def set_name(self,name):
		self._name=name

	def get_id(self):
		return self._id

	def set_id(self,id):
		self._id=id

	def __init__(self,name):
		self._id=Node._next_id
		Node._next_id+=1
		self._name=name
		