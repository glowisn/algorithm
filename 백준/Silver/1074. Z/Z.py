# 1074

def recursion(N, r, c):
    if N == 1:
        if r == 0:
            if c == 0:
                # case 1
                return 0
            elif c == 1:
                # case 2
                return 1
        elif r == 1:
            if c == 0:
                # case 3
                return 2
            elif c == 1:
                # case 4
                return 3
    else:
        mid = 2**(N-1) - 1
        piv = 2**N * 2**N // 4
        if r <= mid and c <= mid:
            # case 1
            return 0 + recursion(N-1, r, c)
        if r <= mid and c > mid:
            # case 2
            return piv + recursion(N-1, r, c-(mid+1))
        if r > mid and c <= mid:
            # case 3
            return piv * 2 + recursion(N-1, r-(mid+1), c)
        if r > mid and c > mid:
            # case 4
            return piv * 3 + recursion(N-1, r-(mid+1), c-(mid+1))


N, r, c = map(int, input().split())

print(recursion(N, r, c))
