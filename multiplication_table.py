#Multiplication table for numbers if 1- 10
st_art = 1
st_op = 10 
count = 1 
st_op2 = 10

while st_art <= 10:  
    if count <= st_op2:
        answer = st_art * count
        print(str(st_art) + " X " + str(count) + "= " + str(answer)) 
        count = count + 1  
    else:
        print('\n')
        st_art = st_art + 1
        count = 1 