nums = input().split()
num1 = int(nums[0])
num2 = int(nums[1])

while True:
    temp = num2
    num2 = num1 % num2
    num1 = temp
    if num2 == 0:
        break
print(num1)
