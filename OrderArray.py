Array = [25,34,98,7,41,19,5]
print(Array)
for i in Array:
	i = 0
	while i < 6:
		x = Array[i]
		if Array[i] > Array[i+1]:
			Array[i] = Array[i+1]
			Array[i+1] = x	
		i += 1
		

print (Array)