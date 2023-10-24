#Calculator
no1 = int(input("Enter no1="))
operator = input(" Choice operation= ( * , / , + , - )\n")
no2 = int (input("Enter no2="))
if(operator == '*'):
    print("Ans=",no1 * no2)
elif(operator =='/'):
    print("Ans=",no1 / no2)
elif(operator == '+'):
    print("Ans=",no1 + no2)
elif(operator == '-'):
    print("Ans=",no1-no2)
else:
    print("Invalid Operator Choose")
