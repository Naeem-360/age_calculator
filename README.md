# 📅 Age Calculator

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained-Yes-brightgreen.svg)](https://github.com/yourusername/age-calculator)

A simple yet powerful Python utility that calculates your exact age in years, months, and days based on your birthdate.

## 🌟 Features

- 📊 Calculates precise age in years, months, and days
- 🗓️ Handles leap years and different month lengths
- 🔄 Automatically compares with the current date
- 🖥️ Clean and user-friendly interface

## 📋 Requirements

- Python 3.x
- `datetime` module (standard library)

## 💻 Usage

Run the script using Python:

```bash
python age_calculator.py
```

Follow the prompts to enter your birth year, month, and day.

## 📝 Example

```
Enter your birth year: 1995
Enter your birth month: 5
Enter your birth day: 15

Your age is:
29 years, 9 months, and 12 days
```

## 🧮 How It Works

The script:
1. Collects the user's birth date information
2. Gets the current date using Python's `datetime` module
3. Performs date calculations with appropriate adjustments for month lengths
4. Displays the precise age in years, months, and days

## 📄 Source Code

```python
from datetime import datetime

# Get current date
today = datetime.now()
current_year = today.year
current_month = today.month
current_day = today.day

# Get birthdate from user
birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

# Calculate age
years = current_year - birth_year
months = current_month - birth_month
days = current_day - birth_day

# Adjust for negative days
if days < 0:
    # Get days in the previous month
    if current_month == 1:  # January
        days += 31  # December has 31 days
    elif current_month == 3:  # March
        if (current_year % 4 == 0 and current_year % 100 != 0) or current_year % 400 == 0:
            days += 29  # February in leap year
        else:
            days += 28  # February in non-leap year
    elif current_month in [5, 7, 10, 12]:  # May, July, October, December
        days += 30  # Previous months have 30 days
    else:
        days += 31  # Previous months have 31 days
    months -= 1

# Adjust for negative months
if months < 0:
    months += 12
    years -= 1

# Display the result
print(f"\nYour age is:")
print(f"{years} years, {months} months, and {days} days")
```

## 📝 Notes

- The script handles date adjustments for accurate calculations
- Works with any valid date input
- Accounts for leap years when calculating February days

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yourusername/age-calculator/issues).

## 📜 License

This project is [MIT](https://opensource.org/licenses/MIT) licensed.

## 🌐 Connect with Me

[![GitHub](https://img.shields.io/badge/GitHub-yourusername-darkgreen.svg)](https://github.com/yourusername)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-yourname-blue.svg)](https://linkedin.com/in/yourname)
