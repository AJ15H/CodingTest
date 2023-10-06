def solution(num_list):
    count=0
    cnt=0
    for i in num_list:
        if i%2==0:
            count+=1
        else:
            cnt+=1
    return count,cnt