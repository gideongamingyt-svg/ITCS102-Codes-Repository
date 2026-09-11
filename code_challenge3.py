#Global Freight Calculator

Name = input("Please Input Your Name:  " )
print("Gideon")

item_type = input("What is the type of items:  "  )
print("Shampoo, Soap, Teethplate, Moisturizers")

fragile = bool(input("Is the item fragile? True or False?  "  ))
print("True")

weight = float(input("Could you provide the weight of the item?  "  ))
print("15")

distance = float(input("How far do it need to travel?  "  ))
print("132")

express = bool(input("Will it travel by express? True or False  "  ))
express = eval(input("Will it travel by express? True or False  "  ))
print("False")

international = bool(input("Will it travel internationaly? True or False?  "  ))
international = eval(input("Will it travel internationaly? True or False?  "  ))
print("True")


base_cost = (weight * 2.50) + (distance * 0.15)


#Free Shipping

if weight <= 2 and distance <= 100 and express == False and international == False:
	print("Free Shipping  ")
	output = 0

#International Express

elif express == True and international == True:
	print("express and international is applied")
	output = (base_cost * 1.40) + 50

#Express of Heavy International

elif express == True or international == True and weight >= 20 and weight <=29.9:
	print("Heavy and Express/International applied")
	output = (base_cost * 1.20) + 25

#Oversized
elif weight >= 30 or distance > 1000:
	print("Oversized package is applied")
	output = base_cost + 30

else:
	print( " base_cost ")
	output = base_cost

print("The total amount due is", output)


# There's an issue where if you type 'false', it turns into true. But once you hit Enter, it goes back to false 