def solution(s):
    if len(s)%2==0:
        num=len(s)//2
        return s[num-1:num+1]
    else:
        return s[len(s)//2]