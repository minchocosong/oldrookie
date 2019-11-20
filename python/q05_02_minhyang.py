def change(x): # x 는 환전할 돈 
    cnt = 0
    if x >= 500: 
        for i in range(15,0,-1):
            if 500 * i < x : 
                y = x - 500*i 
                if y >= 100: 
                    for j in range(15,0,-1):
                        if 100 * j < y:
                            z = y - 100*j
                            if z >= 50:
                                for k in range(15,0,-1):
                                    if 50*k < z:
                                        w = z - 50*k
                                        if w > 10: 
                                            for h in range(15,0,-1):
                                                if 10*h <= w: 
                                                    cnt += 1
                                        else:
                                            cnt += 1 
                                    elif 50*k == z :
                                        cnt += 1 
                            else:
                                 cnt += 1 
                        elif 100 * j == y: 
                            cnt += 1 
                else:
                    cnt += 1 
            elif 500 * i == x: 
                cnt += 1 
    print(cnt)

change(1000)
