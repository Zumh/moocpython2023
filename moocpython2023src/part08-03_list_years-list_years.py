# Write your solution here
# Remember the import statement
# from datetime import date
from datetime import date
def list_years(dates: list):
    years = []
    for each_date in dates:
        years.append(each_date.year)
    years.sort()
    return years
        