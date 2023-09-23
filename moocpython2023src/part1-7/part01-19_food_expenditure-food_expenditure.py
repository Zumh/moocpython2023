"""
Please write a program which estimates a user's typical food expenditure.

The program asks the user how many times a week they eat at the student cafeteria. 
Then it asks for the price of a typical student lunch, and for money spent on groceries during the week.

Based on this information the program calculates the user's typical food expenditure both weekly and daily.

The program should function as follows:


How many times a week do you eat at the student cafeteria? 4
The price of a typical student lunch? 2.5
How much money do you spend on groceries in a week? 28.5

Average food expenditure:
Daily: 5.5 euros
Weekly: 38.5 euros
"""

weekly_freq_eat = int(input("How many times a week do you eat at the student cafeteria? ")) 
lunch_price = float(input("The price of a typical student lunch? "))
weekly_grocery_expense = float(input("How much money do you spend on groceries in a week? "))

daily_expense = ((weekly_freq_eat * lunch_price) + weekly_grocery_expense)/7
weekly_expense = daily_expense * 7

print(f"Average food expenditure: \
\nDaily: {daily_expense} euros \
\nWeekly: {weekly_expense} euros \
")
