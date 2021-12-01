age = input("What is your current age? ")

age_int = int(age)
total_age = 90
year_left = total_age - age_int
days_left = year_left*365
weeks_left = year_left*52
months_left = year_left*12

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
