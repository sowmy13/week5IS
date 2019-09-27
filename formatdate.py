# return formatted date of 3 days from now(no arguments)
#import datetime

from datetime import date,timedelta

def formatdate3days():
    todaysdate = date.today()
    laterdate = todaysdate +timedelta(days=3)
    return laterdate
    
thedate = formatdate3days()
print(thedate)
