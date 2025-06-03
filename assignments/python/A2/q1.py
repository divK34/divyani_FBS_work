# Convert the time entered in hh,min and sec into seconds.

hh = int(input("Enter hours in time : "))
mm = int(input("Enter minutes in time : "))
ss = int(input("Enter seconds in time : "))

hours_in_minutes = hh * 60
minutes_in_seconds = mm * 60

res = (hours_in_minutes * 60) + minutes_in_seconds + ss
print(hh,":",mm,":",ss,"in seconds is",res)