#User inputs height and width to create a box with astericks outling the sides of the box 

#Set It Up 
user_width = int(input("Please type a value to represent the width of your box: "))
user_height = int(input("Please type a value to represent the height of your box: "))
box_outline = '*'
count = 1 

#Work It Out 
if count <= user_height:
        while count == 1: 
            print(user_width * box_outline) 
            count = count + 1 
        
        while count < user_height: 
            number_of_spaces = abs(user_width - 2)
            number_of_spaces = number_of_spaces * ' '
            print(box_outline + number_of_spaces + box_outline) 
            count = count + 1 

        while count == user_height: 
            print(user_width * box_outline) 
            count = count + 1
else: 
 print("end") 

#Finish