#Calculate the total amount (tip + bill amount)
# tip is based on service rating of good, fair, bad
# good: .20 , fair: .15, bad: .10 

#Set It Up 
bill_amount = float(input("Type your bill amount: "))
service_rating = input ("Rate your service by typing on of these options (Good, Fair, or Bad): " ) 
service_rating = service_rating.lower() 

#Work It Out  

#Good Service Output
if service_rating == "good": 
    good = (bill_amount + (bill_amount * .20))  
    good = str(good)
    print("Your total amount is: " + '$' + good + '0') 

#Fair Service Output
elif service_rating == "fair": 
    fair = (bill_amount + (bill_amount * .15)) 
    fair = str(fair) 
    print("Your total amount is: " + '$'+ fair + '0') 

#Bad Service Output
elif service_rating == "bad": 
    bad = (bill_amount + (bill_amount * .10)) 
    bad = str(bad) 
    print ("Your total amount is: " + '$' + bad + '0')

#Invalid Answer Output 
else:
    print ("please type valid answer!")

#Finish