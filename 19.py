import datetime

def sunday_finder(start_year, stop_year):
    counter = 0
    for year in range(start_year, stop_year + 1):
        for month in range(1, 13):
            date = datetime.datetime(year, month, 1)
            if date.weekday() == 6:  
                counter += 1
    return counter

print(sunday_finder(1901, 2000))
