def walk(n):
    if(n==1):
        return 1
    elif(n==2):
        return 2
    else:
        return walk(n-1) + walk(n-2)

print(walk(9))