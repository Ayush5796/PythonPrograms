numbers = []

def get_largest(largest) :
    for num in numbers :
        if largest is None :
            largest = num
        elif (num > largest) :
            largest = num
    print("Maximum is" , largest)

def get_smallest(smallest) :
    for num in numbers :
        if smallest is None :
            smallest = num
        elif (num < smallest) :
            smallest = num
    print("Minimum is", smallest)


while True :
    user_input = input("> ")
    if (user_input == 'done' or user_input == 'Done') :
        break
    else :
        try :
            val = int(user_input)
            numbers.append(val)
        except :
            print("Invalid input")

get_largest(largest = None)
get_smallest(smallest = None)
