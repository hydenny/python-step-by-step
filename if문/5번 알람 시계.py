H, M = input().split()

H = int(H)
M = int(M)

if(M >= 45):
    print("%d %d" %(H, M-45))
else:
    if(H == 0):
        print("%d %d" %(23, M+60-45))
    else:
        print("%d %d" %(H-1, M+60-45))