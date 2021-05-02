print("Compute End Time \n\n")
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))


# Write your code here.
total_start_time = (hour * 60) + mins
total_dura = total_start_time + dura
total_dura_hours = (total_dura // 60) % 24
total_dura_min =  total_dura % 60

print("End Time" , total_dura_hours, ":", total_dura_min)