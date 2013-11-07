def attack(subject,object):
	damage=subject.attack_value-object.defense_value
	if(damage<0):
		damage=0
	object.being_attacked(damage)
