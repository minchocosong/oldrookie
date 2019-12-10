N = 12

def move(log):
    if len(log) == N+1:
        return 1
    
    cnt = 0
    for d in [[0,1],[0,-1],[1,0],[-1,0]]:
        #탐색이 끝나지 않았으면 이동
        next_pos = [log[-1][0]+d[0], log[-1][1]+d[1]]
        # 로그에 다음 위치가 기록되어 있는지 확인 
        check = False
        for p in log:
            if p[0] == next_pos[0] and p[1]== next_pos[1]:
                check=True

        if check == False:
            cnt += move(log+[next_pos])
    return cnt

print(move([[0,0]]))