#Print a triangle / pyramid 
2	
3	#Set it Up
4	triangle_material = '*'
5	count = 1 
6	
7	
8	#Work it Out  
9	while count <= 9: 
10	    x = triangle_material * count
11	    print(x.center(9))
12	    count = count + 2
13	else:
14	 print ('done')
15	
16	#Finish