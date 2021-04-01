import sys 

try: 
  F = float(sys.argv[1])

except: 
  F = float(input('What is the temperature is degrees Fahrenheit?  '))
C = (F - 32)*(5/9)
print(C)