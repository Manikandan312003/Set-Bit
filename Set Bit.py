def setBit(a,b):
    return 0|(1<<a)|(1<<b)
print(setBit(*map(int,input().split())))