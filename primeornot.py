n=int(input("Enter n"))
for i in range(2,100):
    if(n%i==1):
        print("No is prime")
        break;
    else:
        print("No is Not Prime")
        break;