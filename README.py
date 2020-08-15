#Compound Interest 

#Amount in account
print("How much money is in your account?:")
money = float(input('Enter amount:'))

#Years 
print('How many years will you be saving?')
years = int(input('Enter years:'))

#Invested monthly 
print('How many times will the money be compounded annually?: ')
compounded = int(input('Enter amount: '))


#Interest
print('What do you estimate will be the yearly interest of this investment?')
interest = float(input('Enter interest in decimal numbers (10% = 0.1): '))

print(' ')


#Formula 
final_amount = 0 

for i in range(0, years):
	if final_amount == 0:
		final_amount = (money) * (1 + interest/compounded) ** (compounded * years)

print('This is how much you would have in your account after {} years: ''$'.format(years) + str(final_amount))
