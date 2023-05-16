import math

def squares(a, b):
    lower = math.ceil(math.sqrt(a))
    upper = math.floor(math.sqrt(b))
    return upper - lower + 1


if __name__ == '__main__':
    q = int(input().strip())
    results = list()
    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()
        a = int(first_multiple_input[0])
        b = int(first_multiple_input[1])
        results.append(squares(a, b))
    print(*results, end='\n')