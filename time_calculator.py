# add_time("10:10 PM", "3:30")
# 1:40 AM (next day)
def add_time (start: str, duration: str, start_day = "") -> str:
  new_time = ""
  # STEP 1 - Format our parameters into a workable format
  # START - split into 3 parts: hour - minutes - AM/PM
  start_list = start.split() 
  # ['10:10', 'PM']
  start_time = start_list[0].split(':')
  # ['10', '10']
  start_hour = int(start_time[0])
  # 10
  start_minute = int(start_time[1])
  # 10 
  start_meridiem = start_list[1]
  # PM

  # DURATION - split into 2 parts: hour - minutes
  duration_list = duration.split(':')
  # ['3', '30']
  duration_hour = int(duration_list[0])
  # 3
  duration_minute = int(duration_list[1])
  # 30

  # DAY - convert into a standardized string
  day_str = start_day.lower().capitalize()
  
  # STEP 2 - Convert to 24H to perform our calcs, then reformat back to 12H later
  # START - convert to 24H format
  if (start_meridiem == 'PM'):
    start_hour_24 = start_hour + 12
  else:
    start_hour_24 = start_hour
  #22

  # START + DURATION    
  hour_sum = start_hour_24 + duration_hour
  # 25
  minute_sum = start_minute + duration_minute
  # 40 
  
  # STEP 3 - Set up our components: hours, minutes, days, meridiem, message. 
  # Minutes multiple by 60, Hours multiple by 24
  # Start with minutes, to account for the total hours 

  new_minute_sum = 0
  # 40
  new_hour_sum = 0 
  # 1
  day_multiple = 0
  # 1
  new_meridiem = ''
  # AM
  day_message = ''

  weekday_message = ''

  # MINUTES - derive out hours and remaining minutes
  if (minute_sum > 60):
    hour_multiple = minute_sum // 60
    new_minute_sum = minute_sum - (hour_multiple * 60)
    new_hour_sum += hour_sum + hour_multiple 
  else:
    new_minute_sum = minute_sum
    new_hour_sum = hour_sum
  
  # HOURS - derive out days and remaining hours 
  if (new_hour_sum > 24):
    day_multiple = new_hour_sum // 24 
    # 1 (25 total hours / 24 hours = 1 day)
    new_hour_sum = new_hour_sum - (day_multiple * 24) 
    # 1 (25 total hrs - 24 hours = 1 hour remain)
  
  # (DAY MESSAGE) - if day_multiple > 1, display next or # days
  if (day_multiple > 1):
    day_message = f'({day_multiple} days later)'
  elif (day_multiple == 1):
    day_message = '(next day)'
  else: 
    day_message = ''
  # (next day)

  # MERIDIEM - in 24H, AM is 0-12, PM is 13-24. Then convert back to 12H
  if (new_hour_sum > 0) and (new_hour_sum < 12):
    new_meridiem = 'AM'
  elif (new_hour_sum == 12):
    new_meridiem = 'PM'
  elif (new_hour_sum > 12):
    new_meridiem = 'PM'
    new_hour_sum -= 12
  else: # if exactly at 0 in 24H format
    new_meridiem = 'AM'
    new_hour_sum += 12
  # 1 AM

  # STEP 4 - Set up if condition when a day is given 
    
  weekdays_list = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

  if (start_day):
    index_day_given = weekdays_list.index(day_str)
    # Use modulus operator, or calc may exceed list position 0 to 6
    index_new_day = ((index_day_given + day_multiple) % 7)
    weekday_message = weekdays_list[index_new_day] 
    

  # STEP 5 - Put the components together 
  new_minute_format = "{:02d}".format(new_minute_sum)
  
  if (start_day):
    new_time = f'{new_hour_sum}:{new_minute_format} {new_meridiem}, {weekday_message}{day_message}'
  else:
    new_time = f'{new_hour_sum}:{new_minute_format} {new_meridiem} {day_message}'

  new_time = new_time.rstrip()
  
  return new_time 

print(add_time("3:00 PM", "3:10"))
# 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# 12:03 PM

print(add_time("10:10 PM", "3:30"))
# 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12"))
# 7:42 AM (9 days later)