print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice=int(input("Select an operator "))
if (choice>=1 or choice<=4):
      print("Enter two numbers")        
      num1=int(input())
      num2=int(input())    
if choice == 1:
      res = num1+num2
      print (res)
elif choice ==2:
	 res =num1-num2
	 print(res)
elif choice ==3:
	res=num1*num2
	print(res)	   
elif choice==4:
    res = num1//num2
    print(res)  
else:
	print('Invalid input')