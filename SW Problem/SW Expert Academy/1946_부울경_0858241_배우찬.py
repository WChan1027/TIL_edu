t = int(input())

for test_case in range(1,t + 1):
    print("#{}".format(test_case))
    N = int(input())
    result = ''
    k = 0

    for Ci in range(1,N+1):
        Ci, Ki = map(str,input().split())
        Ki = int(Ki)
        result = result + Ci*Ki
        k = k + Ki
    K = k//10

    for i in range(1,K+2):
        print(result[(i-1)*10:i*10].replace(" ",""))