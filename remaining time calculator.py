current_time=input("enter time(format HH:MM):")
total_seconds=86400
entered_hours=int(current_time[0:2])
enetered_minute=int(current_time[3:5])
time_spent_second=(entered_hours*60*60)+(enetered_minute*60)
seconds_left= total_seconds - time_spent_second
print(".............remaiming time..................") 
print(f"Hours={round(seconds_left/3600)}")
print(f"Minutes={round(seconds_left/60)}")
print(f"Seconds={round(seconds_left)}")