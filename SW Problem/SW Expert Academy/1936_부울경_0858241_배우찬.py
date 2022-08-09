a, b = map(int, input().split())


if a == 1:
    if b == 2:
        print('B')
    elif b == 3:
        print('A')
    else :
        print('error')

if a == 2:
    if b == 1:
        print ('A')
    elif b == 3:
        print ('B')
    else :
        print ('error')

if a == 3 :
    if b == 1:
        print ('B')
    elif b == 2:
        print ('A')
    else :
        print('error')

if a != 1 :
    if a != 2 :
        if a != 3:
            print ('error')