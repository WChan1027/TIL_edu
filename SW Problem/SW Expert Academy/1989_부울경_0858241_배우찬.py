n = 1
m = int(input())

while n:
    A1 = list(input())
    A2 = list(reversed(A1))
    if A1 == A2:
        print("#{} 1".format(n))
    if A1 != A2:
        print("#{} 0".format(n))
    if n == m:
        break
    n = n+1