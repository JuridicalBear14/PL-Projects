import random

days = []

months = []

matches = 0

totalMatches = 0

percent = 0

monthNames = ["Placeholder", "January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ]
def datePicker():
    global days
    global months
    for people in range(23):
        month = random.randint(1, 12)
        if month == 4 or month == 6 or month == 9 or month == 11: #30
            day = random.randint(1, 30)
        elif month == 2: #Dumb Febuary
            day = random.randint(1, 28)
        else: #31
            day = random.randint(1, 31)
        days.append(day)
        months.append(month)
        print(monthNames[month], " ", day)
    dateComparator()

def dateComparator():
    global days
    global months
    global matches
    global totalMatches
    person = 0
    people = 0
    for person in range(23):
        for people in range(23):
            if person != people:
                if days[person] == days[people]:
                    if months[person] == months[people]:
                        matches += 0.5
                        totalMatches += 0.5
                        print(months[person], days[person])


        

def single():
    global matches
    global percent
    datePicker()
    #matches = int(matches/2)
    if matches > 1:
        print (matches, " Matches.")
        percent += 1
    elif matches < 1:
        print ("No matches.")
    else:
        print ("1 Match.")
        percent += 1

def multi():
    global totalMatches
    global matches
    global days
    global months
    global percent
    print ("How many times would you like to run it?")
    inputt = int(input())
    for runs in range(inputt):
        single()
        print (" ")
        matches = 0
        days = []
        months = []
    print (int(totalMatches), " Total matches.")
    print ("%", (percent / inputt) * 100, " of runs contained a match")


def highEfficiency():
    global totalMatches
    global percent
    global days
    global matches
    print ("How many times would you like to run it?")
    inputt = input()
    print ("Please wait...")
    for runs in range(int(inputt)):
        for day in range (23):
            days.append(random.randint(1, 365))
        for person in range(23):
            for people in range(23):
                if person != people:
                    if days[person] == days[people]:
                        totalMatches += 0.5
                        matches += 0.5
        if matches > 0:
            percent += 1
            matches = 0
        days = []
    print (int(totalMatches), " Total matches.")
    print ("%", (percent / int(inputt)) * 100, " of runs contained a match")

def compare():
    run = True
    dates = 0
    print ("Input the month of the date you would like to compare (in number form).")
    pMonth = int(input())
    print ("Input the day you would like to compare (in number form).")
    pDay = int(input())
    while run == True:
        month = random.randint(1, 12)
        if month == 4 or month == 6 or month == 9 or month == 11: #30
            day = random.randint(1, 30)
        elif month == 2: #Dumb Febuary
            day = random.randint(1, 28)
        else: #31
            day = random.randint(1, 31)
        print(monthNames[month], " ", day)
        dates += 1
        if int(pMonth) == month:
            if int(pDay) == day:
                run = False
    print (dates, " dates to find ", monthNames[pMonth], " ", pDay, ".")

def startUp():
    inputt = input()
    if inputt == "single":
        single()
    elif inputt == "multi":
        multi()
    elif inputt == "high efficiency":
        highEfficiency()
    elif inputt == "compare":
        compare()
    elif inputt == "description":
        print ("Single makes a random sets of birthdays and tells any matches. Multi runs multiple sets and gives a total percent of how many contained matches. High efficiency is a more streamlined and far faster multi mode (ideal for runs of over 10,000 sets). Compare has the user input a date and runs until it matches that date, then gives a total of how many dates it went through.")
    else:
        print("Please choose single, multi, high efficiency, or compare.")
        startUp()

for spaces in range(10):
    print(" ")
print("Welcome to Parker's birthday generator. Would you like to run single use, multi use, high efficiency, or compare mode? Type description for a    description of each.")
startUp()
