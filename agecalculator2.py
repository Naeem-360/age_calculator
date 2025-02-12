
from datetime import date

birth_year = int(input("Enter Birth year: "))
birth_month = int(input("Enter Birth month: "))
birth_day = int(input("Enter Birth day: "))


today = date.today()

age_years = today.year - birth_year
age_months = today.month - birth_month
age_days = today.day - birth_day

if age_days < 0:
    age_months -= 1
    age_days += 30  

if age_months < 0:
    age_years -= 1
    age_months += 12

print(f"Your age is: {age_years} years, {age_months} months, and {age_days} days.")
