def cutbar(m,n,current): # current는 현재 막대의 수 
    if current >=n: # 현재 막대 개수 >= ncm 막대 막대 개수가 n 개면 다 잘린 것 
        return 0 # 잘라내기 완료
    elif current < m: # 신기신기~~ 막대 수가 사람보다 적으면 다 자를수있음 
        return 1+cutbar(m,n,current*2) # 다음은 현재 2배. 여기서 return 1 + 는 한 번 자르는 횟수 
    else:
        return 1+cutbar(m,n,current+m) # 자를 수 있는 사람 수 만큼 증가 

print(cutbar(3,20,1))
print(cutbar(5,100,1))