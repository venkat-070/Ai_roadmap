def find_max(*numbers):
    result = numbers[0]
    for i in numbers:
        if i > result:
            result = i
    return result
print(find_max(1,2,3,4,5,6))
print(find_max(-5, -2, -10))