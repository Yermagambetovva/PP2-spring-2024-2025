from datetime import datetime, timedelta
today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print(today.strftime("%Y-%m-%d"))
print(yesterday.strftime("%Y-%m-%d"))
print(tomorrow.strftime("%Y-%m-%d"))
