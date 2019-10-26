global count
count = 0


def toh_helper(n, source, via, dest):
    if n == 1:
        global count
        count += 1
        print("Move %s via %s to %s" % (source, via, dest))
        return

    toh_helper(n-1, source, dest, via)
    toh_helper(1, source, via, dest)
    toh_helper(n-1, via, source, dest)


def toh():
    toh_helper(3, 'A', 'B', 'C')


toh()
print(count)
