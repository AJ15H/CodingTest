def solution(money):
    answer = []
    a=money//5500
    answer.append(a)
    answer.append(money-a*5500)
    return answer