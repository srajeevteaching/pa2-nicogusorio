# Programmer: [Nicol ]
# Course: CS701/GB-731, Dr. Rajeev
# Date: [Submission date]
# Programming Assignment: 2
# Program Inputs: [month?year?]
# Program Outputs: [how many days are in a year whether or not it's a leap year]

# ask user for month input
month = input("what month are you asking about in numerical form?")
month = int(month)


# ask user for year input
year = input ("what year are you talking about?")
year = int(year)


# if the month is January, March, May,July,August,October, December
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 412:
    print ("there are 31 days")



# elif the month is April,September, November
elif month == 4 or month == 9 or month == 11:
    print ("there are 30 days")


# elif the month is February
elif month == 2:
    if year % 100 == 0:
        if year % 400 == 0:

            print ("there are 29 days")
        else:
            print ("there are 28 days")
    elif year % 4 == 0:
        print ("there are 29 days")
    else:
        print ("there are 28 days")


# else please enter valid input
else:
    print("sorry, you can't read, please try again")

print("this is where the program ends")


