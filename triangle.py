#Print a triangle / pyramid 

#Set it Up
triangle_material = '*'
count = 1 


#Work it Out  
while count <= 9: 
	x = triangle_material * count
	print(x.center(9))
	count = count + 2
else:
	print ('done')
	
	#Finish