def isgreater(a1, a2, ptr1, ptr2):
    while ptr1 < len(a1) and ptr2 < len(a2) and a1[ptr1] == a2[ptr2]:
        ptr1 += 1
        ptr2 += 1

    if ptr2 == len(a2):
        return True
    if ptr1 < len(a1) and a1[ptr1] > a2[ptr2]:
        return True
    return False


def numb(v, num):
    st = []
    ans = []
    for i in range(len(v)):
        while st and st[-1] < v[i] and len(st) + (len(v)-i-1) >= num:
            st.pop()

        if len(st) < num:
            st.append(v[i])

    while st:
        ans.append(st[-1])
        st.pop()
    ans.reverse()
    return ans


def mergesort(a1, a2):
    merge = []
    ptr1 = 0
    ptr2 = 0

    while ptr1 < len(a1) or ptr2 < len(a2):
        if isgreater(a1, a2, ptr1, ptr2):
            merge.append(a1[ptr1])
            ptr1 += 1
        else:
            merge.append(a2[ptr2])
            ptr2 += 1

    return merge


def optsch(m, g, d, mav, goo):
    res = []
    for i in range(min(m, d) + 1):
        if i <= m and (d-i) <= g:
            v1 = numb(mav, i)
            v2 = numb(goo, d-i)
            res2 = mergesort(v1, v2)
            if isgreater(res2, res, 0, 0):
                res = res2
    return res


def main():
    m, g, d = map(int, input().split())
    mav = list(map(int, input().split()))
    goo = list(map(int, input().split()))
    answer = optsch(m, g, d, mav, goo)
    print(' '.join(map(str, answer)), end="")


if __name__ == "__main__":
    main()
