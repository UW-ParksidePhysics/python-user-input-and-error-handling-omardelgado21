x = []
with open("Fdeg.dat") as file:
    for l in file:
        x.append(l.strip('Fahrenheit degrees:'))
y= [ ]
for i in x:
  y.append((x[i]-32)/1.8);
  n=len(x)
  f = open("degrees.dat", "a")
for i in n:
  f.write(+x[i]+" "+y[i])
  f.write("\n")