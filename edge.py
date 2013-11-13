class Edge:

	_next_id=1

	_id=-1
	_is_directed=False
	_node_id1=-1
	_node_id2=-1

	def get_id(self):
		return self._id

	def set_id(self,id):
		self._id=id

	def __init__(self,is_directed,node_id1,node_id2):
		self._id=Edge._next_id
		Edge._next_id+=1
		self._is_directed=is_directed
		self._node_id1=node_id1
		self._node_id2=node_id2
