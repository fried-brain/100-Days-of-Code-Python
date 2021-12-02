print("Welcome to Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").upper()

bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
elif size == "L":
  bill += 25


add_pepperoni = input("Do you want pepperoni? Y or N ").upper()

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3


extra_cheese = input("Do you want extra cheese? Y or N ").upper()

if extra_cheese == "Y":
  bill += 1


print(f"Your final bill is: {bill}")
