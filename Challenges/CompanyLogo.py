from collections import Counter

#               Short solution:
for item in Counter(sorted(input())).most_common(3):
    print(*item)

#               long solution:
cnt = Counter(sorted(input()))
for item in cnt.most_common(3):
    print(*item)