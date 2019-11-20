cnt = 0

for coin_500 in range(0,2+1): # 500원은 최대 2개 
    for coin_100 in range(0,10+1): # 100원 동전은 최대 10개 
        for coin_50 in range(0,15+1): # 50원 동전은 최대 15개 
            for coin_10 in range(0,15+1): # 10원 동전은 최대 15개 
                if coin_500 + coin_100 + coin_50 + coin_10 <= 15: 
                    if coin_500 * 500 + coin_100*100 \
                        +coin_50 * 50 + coin_10 * 100 == 1000: # \ 줄바꿈 
                        cnt += 1


print(cnt)