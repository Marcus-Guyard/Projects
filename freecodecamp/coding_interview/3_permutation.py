
def perm_alone(str):
    A = str
    perms_list = []

    def generate(n, A):
        A = [c for c in A]
        # c is an encoding of the stack state. c[k] encodes the for-loop counter for when generate(k - 1, A) is called
        c = [0] * n

        b = []
        for char in A:
            if char.isalpha():
                b.append(char)
        perms_list.append(b)

        # i acts similarly to a stack pointer
        i = 1
        while i < n:
            if c[i] < i:
                if i % 2 == 0:
                    A[0], A[i] = A[i], A[0]
                else:
                    A[c[i]], A[i] = A[i], A[c[i]]
                b = []
                for char in A:
                    if char.isalpha():
                        b.append(char)
                perms_list.append(b)
                # Swap has occurred ending the for-loop. Simulate the increment of the for-loop counter
                c[i] += 1
                # Simulate recursive call reaching the base case by bringing the pointer to the base case analog in the array
                i = 1
            else:
                # Calling generate(i+1, A) has ended as the for-loop terminated. Reset the state and simulate popping the stack by incrementing the pointer.
                c[i] = 0
                i += 1

    generate(len(A), A)

    counter = 0
    for _ in perms_list:
        condition = True
        for i in range(len(_)-1):
            if _[i] == _[i+1]:
                condition = False
        if condition:
            counter += 1
    return counter

print(perm_alone('aab'))
