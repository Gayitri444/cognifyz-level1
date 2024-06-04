num1 = eval(input("Enter the num1:"))
num2 = eval(input("Enter the num2:"))
operator = input("Enter the operator:")
if operator == "+":
  print(num1+num2)
elif operator == "-":
  print(num1-num2)
elif operator== "*":  
  print(num1*num2) 
elif operator == "/":
  if num2!= 0:
    print(num1/num2)
  else:
    print("cannot division by zero") 
elif operator == "%":
  print("num1%num2")  
else:
  print("Invalid operator")    

  