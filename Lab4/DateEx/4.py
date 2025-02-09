#program to calculate two date difference in seconds.
from datetime import datetime

#input two dates in the format YYYY-MM-DD HH:MM:SS
date1 = input("first date (YYYY-MM-DD HH:MM:SS): ")
date2 = input("second date (YYYY-MM-DD HH:MM:SS): ")

#convert the input strings to datetime objects
datetime1 = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
datetime2 = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")

difference_in_seconds = abs((datetime2 - datetime1).total_seconds())
print(int(difference_in_seconds))
