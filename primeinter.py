x,y=map(int,input().split())
for i in range(x+1,y):
    if i>1:
        for num in range(2,i):
            if (i%num)== 0:
                break
        else:
            print(i)
