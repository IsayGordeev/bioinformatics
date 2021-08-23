def fibnum(n, k):
    if n is 0 or n is 1:
        return 1
    else:
        return (fibnum(n-1, k) + k * fibnum(n-2, k))

print(fibnum(35,4))