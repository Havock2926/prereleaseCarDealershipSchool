#Task 1
valid_entries = ['y', 'n', 'hatchback', 'estate', 'saloon']
model_options = {
	'Hatchback' : 535000,
	'Saloon' : 495000,
	'Estate' : 625000
}
total_price = 0

is_new = input("Are you a new customer?(y/n)\n> ")
while is_new.lower not in valid_entries:
	print("Invalid input\nTry Again")
	is_new = input("Are you a new customer?(y/n)\n> ")


#conflict
#hei
