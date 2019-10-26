def permute(a, l, r, answer):
    if l == r:
        answer.append(''.join(a))
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]

            permute(a, l+1, r, answer)

            a[l], a[i] = a[i], a[l]


def permutations(S):
    answer = []
    permute(list(S), 0, len(S), answer)

    print(set(answer))


permutations("aaa")


# from itertools import permutations

# permList = list(permutations("199943"))


# for lst in permList:
#     print(''.join(lst))


# print(permList)


print("124".isdigit())


# from itertools import
