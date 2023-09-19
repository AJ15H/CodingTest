def solution(num):
    
    # 입력값이 1이면 바로 반환
    if num==1:
        return 0
    # 500번 반복
    for i in range(500):
        if num%2==0: # 입력값이 짝수
            num=num/2
        else:   # 홀수
            num=num*3+1
        
        if num==1:
            return i+1
        
    return -1
            