from collections import deque

cnt = 0
def change(target,coins,usable):
    global cnt
    coin = coins.popleft() # popleft 리스트의 왼쪽에서부터 절삭하면서 처리 
    if len(coins) ==0: 
        if target // coin <= usable: # 연산자 // : 나누기 연산 후 소수점 이하 수 버리고 정수만 취함, ** : 거듭곱셈, + - * % 는 우리가 아는것 
            cnt += 1 
    else:
        for i in range(0,target // coin + 1):
            change(target- coin*i, coins.copy(),usable-i)

change(1000,deque([500,100,50,10]),15)
print(cnt)

    # deque 함수들 
    # append(x)
    # appendleft(x)
    # extend(iterable) 오른쪽에 iterable arg를 하나씩 추가 ex) ['a','b','c'].extend('df') => ['a','b','c','d','f']
    # extendleft(iterable)
    # pop() : 오른쪽에서 부터 제거와 반환
    # popleft()
    # rotate(n): 요소들을 n의 값만큼 회전 n 이 양수이면 오른쪽 회전 음수이면 왼쪽회전 ['a', 'b', 'c', 'd', 'e'].rotate(2) =>  d e a b c