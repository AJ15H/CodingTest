def solution(start, end_num):
    answer = []

    for num in range(start, end_num-1, -1 ):
        answer.append(num)
    return answer