
try:
    wage = float(input("What is your gross salary? "))
    children = int(input("How many children do you have? "))
#Base tax rate:
    if wage < 1000:
        tax = 10
    elif wage < 2000:
        tax = 12
    elif wage < 4000:
        tax = 14
    else:
        tax = 18
#Tax rate with children;
    if wage < 2000:
        tax = tax - (children * 1)
    else:
        tax = tax - (children * 0.5)

    net_salary = wage * (1 - tax/ 100)

except ValueError:
    print("Please enter numeric values")

print(net_salary)




