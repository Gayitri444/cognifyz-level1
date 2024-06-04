def reverse(string):
  if string == string[::-1]:
    print("Given string is a palindrome:")
  else: 
     print("Given string is not a palindrome:")  

string = input("enter a string:")
print("entered string",string) 
reverse(string)   