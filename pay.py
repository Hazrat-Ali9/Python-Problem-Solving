# Write a program to prompt the user for hours and
# rate per hour to compute gross pay.
# Enter Hours: 35
# Enter Rate: 2.75
# Pay: 96.25

hours = input("Enter number of working hours:")
rate = input("Enter rate per hour:")
try:
    hrs = float(hours)
    r = float(rate)

except:
    print ("Euro, please enter numeric input")
    hours = input("Enter hours:")
    rate = input("Enter rate:")

if hrs > 40:
    pay = 40 *r + (hrs -40)*r*1.5
    print("Pay:",pay)
else:
    pay = hrs * r
    print("Pay:",pay)
