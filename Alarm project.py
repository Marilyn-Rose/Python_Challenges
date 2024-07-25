import time
from datetime import datetime
from plyer import notification

def set_alarm(hour, minute):
    # Let's get the current time
    now = datetime.now()
    alarm_time = datetime(now.year, now.month, now.hour, now.minute)
    
    # Calculate the time difference until the alarm
    time_difference = alarm_time - now
    
    # Wait until the alarm time
    time.sleep(time_difference.total_seconds())
    
    # When the alarm time is reached, trigger the notification and play a sound
    notification.notify(
        title = "Alarm",
        message = "Wake up! You're gonna be late!",
        app_icon = None,
        timeout = 10     # Notification timout in seconds
    )
    return set_alarm(hour, minute)

    
    # Play a sound
    #winsound.Beep(1000, 1000)  # Beep at 1000 Hz for 1 second
    
# 24 hour clock eg 2:24pm
set_alarm(14,7)
