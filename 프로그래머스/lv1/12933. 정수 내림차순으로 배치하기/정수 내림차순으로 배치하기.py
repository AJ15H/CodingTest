def solution(n):
    li=list(map(int, str(n)))
    il=sorted(li, reverse=True)
    answer =''.join(map(str,il))
    result = int(answer)
    return result