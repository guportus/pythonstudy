def is_year_leap(year):
    leap_year = False

    if (year % 4) == 0: #Leap year should be divisible by 4
        leap_year = True
        if(year % 100) == 0 and (year % 400) > 0: #Leap year should be divisible by 100 and 400
            leap_year = False
    
    return leap_year
    
    
test_data = [1900, 2000, 2016, 1987, 2004, 1800,1986]
test_results = [False, True, True, False, True, False,False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
