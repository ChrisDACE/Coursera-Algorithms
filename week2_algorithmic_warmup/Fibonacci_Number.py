index=input()
fb_list=[]
index=int(index)
fb_list.append(int(0))
fb_list.append(int(1))
for i in range(2,index+1):
    fb_list.append(fb_list[i-1]+fb_list[i-2])
print(fb_list[index])