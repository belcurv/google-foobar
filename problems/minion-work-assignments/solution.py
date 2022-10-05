
# Write a function called solution(data, n) that takes in a list of less
# than 100 integers and a number n, and returns that same list but with
# all of the numbers that occur more than n times removed entirely.
# The returned list should retain the same ordering as the original list -
# you don't want to mix up those carefully-planned shift rotations!

# O(n)
def solution1(data, n):
    frequencyMap = dict()
    result = []

    for i in data:
        if i in frequencyMap.keys():
            frequencyMap[i] += 1
        else:
            frequencyMap[i] = 1

    for key,val in frequencyMap.items():
        if val <= n:
            result.append(key)

    # your code here
    return result

# Also O(n)
def solution2(data, n):
    result = []

    for i in data:
        if data.count(i) <= n:
            result.append(i)

    # your code here
    return result

# Also O(n)
def solution3(data, n):
    def filterFn(el):
        return data.count(el) <= n

    return filter(filterFn, data)
