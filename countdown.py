from datetime import datetime, time

hackathon_start = datetime.strptime('2021-04-24 11:30:00', '%Y-%m-%d %H:%M:%S')
hackathon_end = datetime.strptime('2021-04-25 11:30:00', '%Y-%m-%d %H:%M:%S')

# Test date
# now = datetime.strptime('2021-04-24 11:35:00', '%Y-%m-%d %H:%M:%S')

def date_delta(date1, date2):
  time_diff = date1 - date2

  return time_diff.days * 24 * 3600 + time_diff.seconds

def time_left(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	days, hours = divmod(hours, 24)

	return (hours, minutes, seconds)

def print_time():
    message = ''
    
    if datetime.now() < hackathon_start:
        message = "Hackathon has not started yet"
    elif datetime.now() >= hackathon_end:
        message = "Hackathon has ended"
    else:
        hours, mins, secs = time_left(date_delta(hackathon_end, datetime.now()))

        if mins == 0 and hours == 0:
            message = f"{secs} seconds left!"
        elif hours == 0:
            message = f"{mins} mins left!"
        elif mins == 0:
            message = f"{hours} hours left"
        else:
            message = f"{hours} hours {mins} mins left"

    return message
