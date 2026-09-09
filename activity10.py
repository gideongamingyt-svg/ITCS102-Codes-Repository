#logical operator demo

a = 38
b = 9
c = 19

print( a > b and c < a)
print( a > b or c < a)

print( a > b or c < a and c == b)
print( c < a and c == b)
print( not(a > b or c < a and c == b))

#order of precedence
#not, and , or