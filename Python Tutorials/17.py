number1=4
number2=5
number3=6
average=(number1+number2+number3)/3
print(average)


#num1=input("enter the first number")
#num2=input("enter the second number")
#num3=input("enter the third number")



num1,num2,num3=input("enter three numbers comma separated:").split(",")
#(int(num1)+int(num2)+int(num3))/3
print(f"average of three numbers:{(int(num1)+int(num2)+int(num3))/3} ")

