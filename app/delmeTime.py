import datetime
from datetime import datetime
import pytz
from pytz import timezone

# get the current timestamp (YYY-MM-DD HH:MM:SS) and return it to the caller
def get_timestamp():
    now_utc = datetime.now(timezone('UTC'))
    time = now_utc.astimezone(timezone('US/Central'))
    timestamp = time.strftime("%H%M%S")
    return(timestamp)


print(get_timestamp())
