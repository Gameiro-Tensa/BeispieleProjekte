List = [45, 12, 10, 5, 6, 2, 148, 65, 50]

n = len(List)

for i in range(n -1):
    mind_index = i
    for j in range(i + 1, n):
        if List[mind_index] > List[j]:
            mind_index = j
    List[i], List[mind_index] = List[mind_index], List[i]

print(n)
for i in range(n):
    print(List[i], end=" ")