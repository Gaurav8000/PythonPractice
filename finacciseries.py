n=int(input("enter no"))
sum=0
t1=0
t2=1
t3=t1+t2
for i in range(1,n):
    t1=t2
    t2=t3
    t3=t1+t2
    print(t3)

