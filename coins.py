#Coin counter/ printer 

#Set Up 
print("You have 0 coins.")  
coins = 0
give_me = input("Would you like a coin? (Type Yes or no): ") 
give_me = give_me.lower()

# yes is answered
while give_me == "yes": 

    if give_me == "yes": 
        coins = coins + 1
        coins = str(coins)
        print ("You have " + coins + " coins.") 
        coins = int(coins)  
        give_me = input("Would you like a coin? (Type Yes or no): ") 

    else: 
        print ("Toodles.") 
        
else: 
    print ("Goodbye.") 
    

#Finish