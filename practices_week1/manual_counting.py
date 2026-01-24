# Manual counting

numbers = [1,2,3,1,2,3,2,1]

counters = [0] * 3

for num in numbers:
    counters[num - 1] += 1

for i in range(3):
    print(i + 1, counters[i])
