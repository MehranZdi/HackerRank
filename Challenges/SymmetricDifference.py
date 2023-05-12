def symmetric_dif(a, b):
    x = a.difference(b)
    y = b.difference(a)
    # print(x, y)
    z = sorted(x.union(y))
    return z
    

if __name__ == '__main__':
    m = int(input())
    a = set(map(int, input().split()))
    n = int(input())
    b = set(map(int, input().split()))
    result = symmetric_dif(a, b)
    for item in result:
        print(item)


