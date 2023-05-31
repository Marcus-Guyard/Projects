def pairwise(arr, arg):
    sets = []
    used = [False for c in arr]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == arg and not used[i] and not used[j] and i != j:
                sets.append((i, j))
                used[i] = True
                used[j] = True
    total = [sum(n) for n in sets]
    return sum(total)

print(pairwise([1, 4, 2, 3, 0, 5], 7))