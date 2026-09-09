import getpass 

username = 'palcisomewing'
password = 'handsomemewing'

u = input('Input Username ---> ')
p = getpass.getpass('Input Password ---> ')

if username == u and p == password : 			
	print("ACCESS GRANTED")
else: 
	print("ACCESS DENIED")