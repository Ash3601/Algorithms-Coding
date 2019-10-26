def _getNthFib(n):
    # Write your code here.
    if n <= 1:
        return n - 1
    return getNthFib(n-1) + getNthFib(n-2)


def getNthFib(n):
    first = 0
    second = 1
    if n == 1:
        print(first)
        return
    elif n == 2:
        print(second)
        return
    for _ in range(3, n+1):
        current = first + second
        first = second
        second = current
    print(current)


# for i in range(1, 10):
#     getNthFib(i)
getNthFib(1)
