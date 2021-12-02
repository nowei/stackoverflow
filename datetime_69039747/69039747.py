import time

t1 = time.strptime("10:00 AM IST", "%I:%M %p %Z")
t2 = time.strptime("11:00 AM IST", "%I:%M %p %Z")
t3 = time.strptime("12:00 AM IST", "%I:%M %p %Z")
t4 = time.strptime("10:30 AM IST", "%I:%M %p %Z")
print(t1 <= t3 <= t2) # false
print(t1 <= t4 <= t2) # true