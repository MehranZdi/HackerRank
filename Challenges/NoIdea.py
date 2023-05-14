#               Pythonic and efficient solution:

n, m = input().split()
arr = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))

print(len(list(filter(lambda x: x in a, arr))) - len(list(filter(lambda x: x in b, arr))))


#                Inefficient solution:

def happiness_counter(arr, a, b):
    happiness = 0
    for item in arr:
        if item in a:
            happiness += 1
        elif item in b:
            happiness -= 1
    return happiness


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    n, m = nums[0], nums[1]
    arr = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    result = happiness_counter(arr, a, b)
    print(result)