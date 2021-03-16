inputs = input().split()
index = int(inputs[0])
divisor = int(inputs[1])

pisano = [0,1]
length=2

for i in range(2, index + 1):
    pisano.append((pisano[i - 1] + pisano[i - 2]) % divisor)
    length+=1
    if pisano[i-1]==0 and pisano[i]==1:
        break

if length==index+1:
    print(pisano[index])
else:
    print(pisano[index%(length-2)])

