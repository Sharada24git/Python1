num1=int(input("Multiplier Start: "))
num2=int(input("Multiplier End: "))
tstart=int(input("Multiplicand Start: "))
tend=int(input("Multiplicand End: "))
for j in range(tstart,tend+1,1):
    for i in range(num1,num2+1,1):
        print(i,j,i*j)
    print()
