#Allowing the bill to be split by user inputted amount 

#Set it up 
bill_amount = input("Please type the amount of your bill: ")
bill_amount = float(bill_amount)

number_of_people = input("Please enter number of people at your table: ") 
number_of_people = float(number_of_people)

#Work it Out  
amount_per_person = bill_amount / number_of_people 
amount_per_person = "%.2f" % amount_per_person 
amount_per_person = str(amount_per_person) 
amount_per_person = "Amount per person: "+ "$" + amount_per_person
print (amount_per_person)


#Finish