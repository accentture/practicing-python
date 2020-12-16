
numbers = [6,4,4,7,8,23,87]

#this snippet code can generate an error therefore I put in a try
try:
    search = int(input("Enter some number: "))

    check = isinstance(search, int) #checking if search is entire type
    while not check or search <= 0 :
        search = int(input("Enter some number: "))
    else :
        print(f"You has introduced the {search}")

    print(f" #### Searching in the list the number {search} ####")

    otherSearch = numbers.index(search) # get index of the number passed as param
    print(f"the number searched exists in the list, it is the index: {otherSearch}")

#to mangament error if number isn't in the list
except:
    print("The number {search} isn't in the list, sorry!!")


