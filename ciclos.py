abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(26,0,-1):
    print("")
    for j in range (i,0,-1):
        print(abc[j-1],end='')
