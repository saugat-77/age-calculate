from datetime import date

input_year=int(input("input your year: "))
input_month=int(input("input your month: "))
input_day=int(input("input your day: "))

first_time=date(input_year,input_month,input_day)
current_time=date.today()

delta=current_time-first_time
x=delta.days
x=x/365
year=int(x)
y= x-year
month=int(y*12)
y=y%12
days=int(y*30)
year=str(year)
month=str(month)
days=str(days)

print("You are " +year+ " years " +month+" months " +days+ " days old.")
print("good luck on that buddy !!")
