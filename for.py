x=int(input("number"))
for i in range(1,x):
    for j in range(1,x-i):
        print(' ',end='')
    for m in range(i,0,-1):
        print(m,end='')
    for k in range(2,i+1):
        print(k,end='')
    print()
print("end")
