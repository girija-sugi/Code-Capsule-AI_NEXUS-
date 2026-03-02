numbers = list(map(int, input().split()))
print(numbers)
evenNumbers=[]
def sum_of_evens(num: list[int]) -> int:
    for i in num:
        if i%2==0:
            evenNumbers.append(i)
    print(evenNumbers)
    return sum(evenNumbers)
sum = sum_of_evens(numbers)
print(sum)

