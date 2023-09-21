def solution(s):
    a=[]
    s_li=list(s.split(' '))
    
    for i in s_li:
        a.append(i.capitalize())
    answer = ' '.join(a)
        
    
    
    return answer
    # return s.title()