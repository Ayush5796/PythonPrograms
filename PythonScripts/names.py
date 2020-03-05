from name_function import get_formatted_name

print("Enter 'q' to quit any time")

while(True):
    first = input("Enter your First Name: ")
    if first == 'q':
        break

    last = input("Enter your Last Name: ")
    if last == 'q':
        break;
    
    formatted_name = get_formatted_name(first, last)
    print("\tNeatly Formatted Name: " + formatted_name)