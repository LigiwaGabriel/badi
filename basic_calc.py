
# Conditional Statements

age=int(input("Enter your age"))
if age>=18:
    print("You are and adult")
else:
    print("Your a child")

## EXAMPLE TWO 
"""
IF, ELSE IF, ELSE 

"""
print("select your age: \n1. 18 and above. \n2. 17 and below \n")
age=int(input("Please make your choice: "))

if age==1:
    print("You are an adult")
elif age==2:
    print("Your a child: ")
else:
    print("Provide a valid age range")

#EXAMPLE THREE 
print("MENU")
print("1. + \n2. - \n3. x \n4. /")
operator_selection=int(input("Please make your choice:"))
first_number= float(input("Enter the first number"))
second_number= float(input("Enter the second number"))

if operator_selection==1:
    summation= first_number+second_number
    print(f"The sum is {summation}")

elif operator_selection==2:
    difference=(first_number-second_number)
    print(f"The difference is,{difference}")

elif operator_selection==3:
    product=(first_number*second_number)
    print(f"The product is, {product}")

elif operator_selection==4:
    quotient=(first_number/second_number)
    print(f"the quotient is {quotient}")
    



