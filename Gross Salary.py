salary = input("Please give me your salary ")
try:
    salary = float(salary)

    if salary < 1000:
        tax = salary*0.1
    elif salary < 2000:
        tax = salary*0.12
    elif salary < 4000:
        tax = salary*0.14
    else:
        tax = salary*0.18

    before_child = salary - tax
    print(f"Your net salary before child tax breaks is {before_child}")

    children = input("How many children do you have? ")
    children = int(children)
    if salary < 2000:
        tax_child = 0.01*children*salary
    else:
        tax_child = 0.005*children*salary

    print(f"Your final net salary is {before_child+tax_child} and your total tax break for having children is of {tax_child}")

except:
    print("Give me a valid number")