# Check leap year
#Leap year is sequence of every 4 years so it should be only divisble by 4 or 400 but not divisble by 100 to check if its a leap year or not.
def leap_year_check(yr):
    if (yr % 4 == 0 and yr % 100 != 0) or (yr % 400 == 0) == 0:
        print("Its a leap year")
    else:
        print("Its not a leap year")
leap_year_check(1700)
