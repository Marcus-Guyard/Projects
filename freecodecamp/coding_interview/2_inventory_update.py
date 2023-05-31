def update_inventory(arr1, arr2):
    if len(arr1) == 1:
        return sorted(arr2, key=lambda x: x[1])
    if len(arr2) == 1:
        return sorted(arr1, key=lambda x: x[1])
    inventory = []
    obj = []
    arr = arr2 + arr1
    print()
    for r in arr1:
        for l in arr2:
            if r[1] == l[1]:
                r[0] += l[0]
                inventory.append(r)
                obj.append(r[1])
    for _ in arr:
        if _[1] not in obj:
            inventory.append(_)
    return sorted(inventory, key=lambda x: x[1])


cur_inv = [
    []
]
new_inv = [
    [2, "Hair Pin"], [3, "Half-Eaten Apple"], [67, "Bowling Ball"], [7, "Toothpaste"]
]
print(update_inventory(cur_inv, new_inv))