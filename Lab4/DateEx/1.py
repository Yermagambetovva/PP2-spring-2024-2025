from datetime import datetime, timedelta 
current_day = datetime.now()
to_fivedays = current_day - timedelta(days=5)
print(current_day.strftime("%Y-%m-%d"))
print(to_fivedays.strftime("%Y-%m-%d"))