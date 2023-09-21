def solution(n):
    li=list(map(int, str(n)))
    il=sorted(li, reverse=True)
    answer =int(''.join(map(str,il)))
    # result = int(answer)
    return answer
    
    # ls = list(str(n))
    # ls.sort(reverse = True)
    # return int("".join(ls))