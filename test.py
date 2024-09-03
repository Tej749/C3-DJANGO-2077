def sums(*data):
    sum = 1
    for value in data:
        sum = sum * value
    print(sum)

sums(2, 4, 6)