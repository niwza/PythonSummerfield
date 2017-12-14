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

sorted_list = []
while numbers:
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    sorted_list.append(numbers.pop(numbers.index(minimum)))

index = len(sorted_list) // 2
if len(sorted_list) % 2 == 1:
    median = sorted_list[index]
else:
    median = (sorted_list[index] + sorted_list[index - 1]) / 2

print("count =", count, "sum =", total, "lowest =", lowest, "highest =", highest, "mean =", mean, "median =", median)
