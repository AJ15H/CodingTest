def solution(n, k):
    if n<10:
        return n*12000+k*2000
    else:
        service = n//10
        return n*12000+(k-service)*2000