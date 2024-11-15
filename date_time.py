import datetime

my_bday = datetime.date(2000, 1, 1)

print("My bday is:" , my_bday)
print("My bday year is:" , my_bday.year)
print("My bday month is:" , my_bday.month)
print("My bday day is:" , my_bday.day)

# python default format: YYYY-MM-DD

print("I was born on:" , my_bday.strftime("%A, %B %d, %Y")) # I was born on: Friday, January 01, 1993

# date_time_arr = dir(datetime)
# print(date_time_arr)
# print(help(datetime.date))

# Space X first launched its reusable rocket on March 30 , 2017 , 22:27 UTC

launch_date = datetime.date(2017, 3, 30) # using date class
launch_time = datetime.time(22, 27, 0) # using time class
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0) #using datetime class

print(launch_date) # 2017-03-30
print(launch_time) # 22:27:00
print(launch_datetime) # 2017-03-30 22:27:00

# To get today's date
now = datetime.datetime.today()
print("now:" , now )
print("now in micro seconds:" , now.microsecond)