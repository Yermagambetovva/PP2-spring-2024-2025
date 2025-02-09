#program to drop microseconds from datetime.
from datetime import datetime
current_datime = datetime.now()
datetime_without_microseconds = current_datime.replace(microsecond=0)
print(current_datime)
print(datetime_without_microseconds)
