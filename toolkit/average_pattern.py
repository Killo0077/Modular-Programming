total = 0
count = 0

for n in numbers:
    if n < 50:
        total += n
        count += 1

if count > 0:
    average = total / count
    print(average)