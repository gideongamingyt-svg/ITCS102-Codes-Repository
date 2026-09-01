money = 8935

print("money to deposit", money)
 
print(" ==================== PH PESO DENOMINATION BREAK DOWN ====================== CURRENT MONEY IS ----> ", money, "php")

libo = money // 1000 #069 -> how to bring down value 8.935
libo_sukli = money % 1000 #935

five_h = libo_sukli // 500
five_sukli = libo_sukli % 500

two_h = five_sukli // 200
two_sukli = five_sukli % 200

one_h = two_sukli // 50
one_sukli = two_sukli % 50

zero_h = one_sukli // 5
zero_sukli = one_sukli % 5

print("1000 - ", libo)	
print("500 - ", five_h)
print("200 - ", two_h)
print("100 - ", two_h)
print("50 - ", one_h)
print("20 - ", one_h)
print("10 - ", one_h)
print("5 - ", zero_h)
print("1 - ", zero_h) 