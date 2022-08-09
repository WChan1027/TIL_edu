N = int(input())

a = N//1000
b = (N-a*1000)//100
c = (N-a*1000-b*100)//10
d = (N-a*1000-b*100-c*10)

print(a+b+c+d)