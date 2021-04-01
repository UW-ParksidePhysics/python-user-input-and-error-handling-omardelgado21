infile = open ('f2c_qa.py', 'r')
infile.readline()
infile.readline()
infile.readline()

F = float(input(((infile.readline()).split())[2]))
infile.close()
C = (F - 32)*(5/9)
print(C)

