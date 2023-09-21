def solution(x):
    divisor=0
    x_li=list(map(int,str(x)))
    
    for i in x_li:
        divisor += i
    if x%divisor==0:
        return True
    else:
        return False
    
   