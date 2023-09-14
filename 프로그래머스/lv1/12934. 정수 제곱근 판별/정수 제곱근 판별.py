def solution(n):
    answer = n**(0.5)
    if answer%1==0:
        result =(answer+1)**2
        return result
    return -1