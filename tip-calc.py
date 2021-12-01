bill = float(input("What is your bill amount? \n"))
tip_percentage = int(input("What percentage tip would you like to pay? 10, 12, 15 ? \n"))

people = int(input("In between how many peple would you like to split the bill? \n"))

amount = float(bill*(1 + tip_percentage/100))

amount_perperson = "%.2f"%(amount/people)

print(f"Each person should pay: ${amount_perperson}")
