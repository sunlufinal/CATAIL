from networkx import nx
from person import *
from action import *

# a=Person()
# b=Person()
# a.attack_value=100
# b.defense_value=30
# attack(a,b)
# if(b.is_alive):
# 	print("b is still alive")
# else:
# 	print("b is dead")
# attack(a,b)
# if(b.is_alive):
# 	print("b is still alive")
# else:
# 	print("b is dead")

###global initialization
world=nx.Graph()
next_id=1
list_of_node=[]

tmp=Person(next_id)
next_id+=1
list_of_node.append(tmp)

