import calendar
from datetime import datetime

hoje = datetime.now()
calendar.setfirstweekday(calendar.SUNDAY)
matrix = calendar.monthcalendar(hoje.year, hoje.month+2)

print(matrix)