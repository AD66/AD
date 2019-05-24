class information:
	def __init__(self, name, age,height, weight):
		self.name=name
		self.age=age
		self.weight=weight
		self.height=height
obj1=information("Adarsh", 23, 5.9, 79)
obj2=information("Sagar", 26, 6.0, 84)

print("Age of {} is {}".format(obj1.name,obj1.age))
print("Age of {} is {}".format(obj2.name,obj2.age))
print("Height of {} is {}".format(obj1.name,obj1.height))
print("Height of {} is {}".format(obj2.name,obj2.height))
print("Weight of {} is {}".format(obj1.name,obj1.weight))
print("Weight of {} is {}".format(obj2.name,obj2.weight))




