import sys

inputs=sys.stdin.read()
tokens=inputs.split()
nums=[]
for item in tokens:
    nums.append(int(item))
length=nums.pop(0)


nums_sorted=sorted(nums,reverse=True)
print(nums_sorted[0]*nums_sorted[1])

