def is_year_leap(year):
    leap_year = False

    if (year % 4) == 0: #Leap year should be divisible by 4
        leap_year = True
        if(year % 100) == 0 and (year % 400) != 0: #Leap year should be divisible by 100 and 400
            leap_year = False
    
    return leap_year

def days_in_month(year, month):
    odd_month = [1,3,5,7,8,10,12]

    if month < 12 :
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

test_years = [1900, 2000, 2016, 1987, 1990]
test_months = [2, 2, 1, 11, 15]
test_results = [28, 29, 31, 30, None]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")