from datetime import date
print("1. My birthday is today ")
print("2. My birth year is ")
options = input("Please choose option 1 or 2 ")


def age():
    current_year = int(date.today().year)
    birth_year = int(input("What year were you born? "))
    years = current_year - birth_year
    print("You are " + str(years) + " years old")


if options == "1":

    print("Happy birthday!!!")
    age()
elif options == "2":
    age()
