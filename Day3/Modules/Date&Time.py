import datetime

x = datetime.datetime.now()
print(x)

print(x.day)
print(x.year)

# The datetime object has a method for formatting date objects into readable strings.
# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string
print(x.strftime("%A")) # name of weekday

x = datetime.datetime(1999, 1, 1)
print(x.strftime("%A")) # Friday
