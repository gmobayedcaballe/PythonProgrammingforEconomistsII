numbers_list = list(range(1,11))
multiplier = 10
for times in range(1,11):
    for i in numbers_list:
        print(f"{i} * {multiplier} = {i*multiplier}")
    numbers_list.pop()
    multiplier -= 1





