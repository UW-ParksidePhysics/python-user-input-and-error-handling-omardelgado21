import sys 

try:
 F = float(input(sys.argv[1]))
 C = (F - 32)*(5/9)
 print(C)

except IndexError:
  print('Error! Temperature in degrees Fahrenheit was not provided.')