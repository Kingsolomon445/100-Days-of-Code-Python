# Days in Month

def is_leap(given_year):
    if given_year % 400 == 0 or (given_year % 4 == 0 and given_year % 100 != 0):
        return True
    else:
        return False


def days_in_month(given_year, given_month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(given_year):
        if given_month == 2:
            return month_days[given_month - 1] + 1
    return month_days[given_month - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
