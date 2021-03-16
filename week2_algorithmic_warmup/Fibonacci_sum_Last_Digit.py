index = int(input())
fb_list = [0, 1]

if index <= 1:
    print(fb_list[index])
else:
    pisano = [0, 1]
    length = 2
    while True:
        pisano.append((pisano[length - 1] + pisano[length - 2]) % 10)
        length += 1
        if pisano[length - 2] == 0 and pisano[length-1] == 1:
            break
    length = length - 2
    pisano=pisano[:-2]
    sum_periodic=sum(pisano)%10

    sum_extra=0
    for i in range((index+1)%60):
        sum_extra+=pisano[i]%10

    print(((index+1)//60*sum_periodic+sum_extra)%10)

