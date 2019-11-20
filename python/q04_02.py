def cutbar(m,n): # m 명이 n cm 를 붙여 만듦
    count =0
    current = 1 # current 현재길이 
    while n > current: # n cm 될 때까지
        current += current if current < m else m # python if else one line 으로 쓰기 if 조건 만족할 떄 앞에 값, else 일 때 뒤에 값 
        count += 1
    print(count)

cutbar(3,20)
cutbar(5,100)
