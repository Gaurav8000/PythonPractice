n=int(input("enter number"))
rev=0
rem=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("reverse no is=",rev)