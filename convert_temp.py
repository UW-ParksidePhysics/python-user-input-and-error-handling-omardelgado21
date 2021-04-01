#converting Celcius to Fahrenheit
def C2F(C): 
  F = 32 + C*(9/5)
  return F 

#converting Fahrenheit to Celcius
def F2C(F):
  C = (F - 32)*(5/9)
  return C

#converting Celcius to Kelvin
def C2K(C):
  K = 273 + C
  return K

#converting Kelvin to Celcius
def K2C(K):
  C = K - 273
  return C

#converting Fahrenheit to Kelvin
def F2K(F):
  K = 273 + F2C(F)
  return K

#converting Kelvin to Fahrenheit
def K2F(K):
  F = C2F(K) - 273
  return F

if __name__ == '__main__':
  C = 100 
  print(C, C2F(C), C2K(C))
  F = 100 
  print(F, F2C(F), F2K(F))
  K = 100 
  print(K, K2C(K), K2F(K))