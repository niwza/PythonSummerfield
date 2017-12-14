numbers = []
total = 0
lowest = None
highest = None

while True:
    num = input("enter a number or Enter to finish: ")
    if not num:
        break
    try:
        i = int(num)
        if lowest is None or i < lowest:
            lowest = i
        if highest is None or i > highest:
            highest = i
        numbers += [i]
        total += i
    except ValueError:
        print("Please enter a valid integer.")
        continue

count = len(numbers)
mean = total / count

print("numbers: ", numbers)
print("count =", count, "sum =", total, "lowest =", lowest, "highest =", highest, "mean =", mean)
