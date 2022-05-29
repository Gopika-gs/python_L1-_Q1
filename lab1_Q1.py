from datetime import date
name = input("Enter your name ")
age = int(input("Enter your age "))
today = date.today()
year = (100 - age) + today.year
print("Hello " + name + " it's nice to meet you! ")
print ("you will turn 100 years old in " , year)