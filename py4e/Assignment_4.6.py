def computepay(hrs, rate) :
    if (hrs <= 40) :
        pay = hrs * rate
    else :
        pay = (40 * rate) + ((hrs - 40) * (rate * 1.5))

    return pay


hours = input("Enter hours : ")
rate_per_hour = input("Enter the Rate : ")

try:
    hrs = float(hours)
    rate = float(rate_per_hour)
except :
    print("Invalid input!!")
    quit()

pay = computepay(hrs, rate)

print("Pay :" , pay)
