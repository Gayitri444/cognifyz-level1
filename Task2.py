Temperature = eval(input("Enter the temperature:"))
unit = input("Enter the units(celsius or fahrenheit):")
if unit == "celsius":
  converted_temperature = (Temperature*9/5)+32
  print(f"The temperatue in Fahrenheit is:{converted_temperature}F" )
elif unit == "fahrenheit":
  converted_temperature = (Temperature*5/9)-32
  print(f"The temperture in Celsius is:{converted_temperature}C")
else:
  print("Invalid unit of measurement:")  


