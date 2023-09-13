# def solution(arr):
#     sum=0
#     cnt=0
    
#     for i in range(len(arr)):
        
#         sum += arr[i]
#         cnt += 1
        
#     avg = sum/cnt
    
#     return avg

def solution(arr):
    sum=0
    cnt=0
    
    for i in arr:
        
        sum += i
        cnt += 1
        
    avg = sum/cnt
    
    return avg
