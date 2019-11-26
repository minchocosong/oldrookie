count = 0

def collatz(basic, now):
    if(now%2==0) : 
        if(now/2==basic): 
            return 1 
        elif(now/2>basic): 
            return collatz(basic,now/2)
        else:
            return 0
    else: 
        if(now*3+1 == basic): 
            return 1
        elif(now*3+1 > basic):
           return collatz(basic,now*3+1)
        else: 
            return 0


for candi in range(2,1000+1,2):
    count += collatz(candi,3*candi+1)

print (count)

