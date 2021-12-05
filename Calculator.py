num1=int(input("Enter number1 :"))
num2=int(input("Enter number2 :"))
print("1.Adittion\n 2.Subtraction\n  3.Multyply\n   4.Divide")
ch=int(input("Enter your choice"))
if("ch==1"):
    sum=num1=num2
    print("Sum =",sum)
elif("ch==2"):
    diff=num1-num2
    print("Difference =", diff)
elif("ch==3"):
    Mul=num1*num2
    print("Multyplication =",mul)
elif("ch==4"):
    if(num2==0):
        print("Division not valid")
else:
    div=num1/num2
    print("Division =",div)