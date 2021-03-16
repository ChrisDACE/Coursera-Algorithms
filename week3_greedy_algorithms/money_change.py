total_val=int(input())
count=0
curr_val=0
deno=[10,5,1]
i=0

while curr_val<total_val:
    if total_val-curr_val>=deno[i]:
        curr_val+=deno[i]
        count+=1
    else:
        i+=1
print(count)
