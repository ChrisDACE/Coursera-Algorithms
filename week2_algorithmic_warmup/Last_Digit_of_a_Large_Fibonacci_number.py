index=input()
index=int(index)
last_digit=[]
last_digit.append(0)
last_digit.append(1)
for i in range(2,index+1):
    last_digit.append((last_digit[i-1]%10+last_digit[i-2]%10)%10)
print(last_digit[index])