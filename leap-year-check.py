#taking input
year = int(input("Which year do you want to check? \n"))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print(f"{year} is a Leap year.")
    else:
      print(f"{year} is not a Leap year.")
  else:
    print(f"{year} is a Leap year.")
else:
  print(f"{year} is not a Leap year.")
