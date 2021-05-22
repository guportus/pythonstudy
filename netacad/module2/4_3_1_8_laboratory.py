# Netacad exercise 4.3.1.6
# Check if year is leap year
# Added days in year

def is_year_leap(year):
    leap_year = False

    if (year % 4) == 0: #Leap year should be divisible by 4
        leap_year = True
        if(year % 100) == 0 and (year % 400) != 0: #Leap year should be divisible by 100 and 400
            leap_year = False
    
    return leap_year

def days_in_month(year, month):
    odd_month = [1,3,5,7,8,10,12]

    if month <= 12 :
        if month in odd_month:
            return 31
        else:
            if month == 2:
                if is_year_leap(year):
                    return 29
                else:
                    return 28
            else:
                return 30
    
    return None

def valid_date(year, month, day):
    if days_in_month(year, month) != None and day <= days_in_month(year,month):
        return True
    else:
        return False

        
def day_of_year(year, month, day):

    days = 0
    
    if valid_date(year,month,day):
        for mon in range(1, month):
            days += days_in_month(year, mon)
        
        days += day
    else:
        return None

    return days

#Test data
print(day_of_year(2000, 12, 31))
print(day_of_year(2001, 12, 31))
print(day_of_year(2024,3,28))
print(day_of_year(2023,3,28))
