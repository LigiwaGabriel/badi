# Amina's Market Receit Calculator 
print("Amina's Market Receit") 
item=input("Enter the name of the item")
Price=float(input("Enter the price per kilogram"))
kilograms=float(input("Enter the number of kilograms purchased"))
total_cost=(Price*kilograms) # This multiplies the price by the number of kgs bought
Discount=(0.1*total_cost) # this gets the amount to be discounted 
print(Discount)
final_price=(total_cost-Discount) #this subtracts the discount from the price to get the net price 
print(final_price)

#Bill splitting
split=3
per_person=(final_price/split) # This divides the final price by split 
print(per_person)
remainder=(final_price%split) #this uses the modulus operator to find the remainder 
print(remainder)
share_floor=(final_price//split)
print(share_floor)

# QUESTION 2

# Sports Day Scoreboard: Relational Operators 
eagle_score=78
falcon_score=85
print(eagle_score)
print(falcon_score)

print(eagle_score>falcon_score)
print(eagle_score<falcon_score)
print(eagle_score==falcon_score)
print(eagle_score!=falcon_score)
print(eagle_score>=75)
print(falcon_score<=80)

# Scorers From user input
input("Enter a new eagle score")
input("Enter a new falcon score")
print(eagle_score>=falcon_score)
print(eagle_score==falcon_score)

# Summary Statistics

difference=float(input(falcon_score-eagle_score))
print(difference)
combined=float(input(falcon_score+eagle_score))
print(combined)
avergae=float(input(eagle_score+falcon_score/2))
print(avergae)





