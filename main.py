from person import *
from action import *

a=Person()
b=Person()
a.attack_value=100
b.defense_value=30
attack(a,b)
if(b.is_alive):
	print("b is still alive")
else:
	print("b is dead")
attack(a,b)
if(b.is_alive):
	print("b is still alive")
else:
	print("b is dead")
