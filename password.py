#importing random

import random


#characers allowed in password
chars="qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJGFDSAZXCVBNM1234567890!@#$%^&*?/"

password_len=int(input("length of password:  "))
password=" "
for x in range(0,password_len): 
			password_char=random.choice(chars)
			password=password+password_char
	
print("here is random password:",password)
