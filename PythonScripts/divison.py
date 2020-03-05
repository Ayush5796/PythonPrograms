print("Division Calculator!!!")
print("Enter 'q' to quit!!")
while True:
    first_number = input("Enter the first number: ")
    if(first_number == 'q'):
        break
    second_number = input("Enter the second number: ")
    if(second_number == 'q'):
        break

    try:
        anwser = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("The first number can not be divided by zero!!!")
    else:
        print(anwser)



