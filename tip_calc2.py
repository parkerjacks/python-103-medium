#Allowing the bill to be split by user inputted amount 

#Set it up 
bill_amount = input("Please type the amount of your bill: ")
bill_amount = float(bill_amount)

number_of_people = input("Please enter number of people at your table: ") 
number_of_people = float(number_of_people)

service_rating = input("Please rate your service (Good, fair, bad): ") 
service_rating = service_rating.lower() 




#Work it Out   
if service_rating == "good":  

    #Calculate Good service total
    tip_amount = bill_amount * .20 
    total_amount = bill_amount + tip_amount 
    amount_per_person = total_amount/number_of_people

    #Turn the above into strings
    tip_amount = str(tip_amount) 
    total_amount = str(total_amount) 
    amount_per_person = str(amount_per_person)

    #Output
    print ("Tip Amount: " + tip_amount + '\n' + "Total Amount: " + total_amount + '\n' + "Amount per person: " + amount_per_person) 

elif service_rating == "fair":

    #Calculate fair service total
    tip_amount = bill_amount * .15 
    total_amount = bill_amount + tip_amount 
    amount_per_person = total_amount/number_of_people 

    #Turn the above into strings
    tip_amount = str(tip_amount) 
    total_amount = str(total_amount) 
    amount_per_person = str(amount_per_person) 

    #Output
    print ("Tip Amount: " + tip_amount + '\n' + "Total Amount: " + total_amount + '\n' + "Amount per person: " + amount_per_person) 


elif service_rating == "bad": 

    #Calculate bad service total
    tip_amount = bill_amount * .10 
    total_amount = bill_amount + tip_amount 
    amount_per_person = total_amount/number_of_people

    #Turn the above into strings
    tip_amount = str(tip_amount) 
    total_amount = str(total_amount) 
    amount_per_person = str(amount_per_person) 

    #Output
    print ("Tip Amount: " + tip_amount + '\n' + "Total Amount: " + total_amount + '\n' + "Amount per person: " + amount_per_person) 

 
    



#Finish