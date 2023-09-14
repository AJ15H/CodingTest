# def solution(survey, choices):
#     data = ["R", "T", "C", "F", "J", "M", "A", "N"]
#     score = [0 for str in data]
#     result = ''
    
#     for i in range(len(survey)):
        
#         if 4<choices[i]<=7:
#             score[data.index(survey[i][-1])] += choices[i]-4
#         if choices[i]==4:
#             pass
#         if 1<=choices[i]<4:
#             score[data.index(survey[i][0])] += 4-choices[i]
            
    
#     if score[0]<score[1]:
#         result1=data[1]
#     else:
#         result1=data[0]
        
#     if score[2]<score[3]:
#         result2=data[3]
#     else:
#         result2=data[2]
        
#     if score[4]<score[5]:
#         result3=data[5]
#     else:
#         result3=data[4]
    
#     if score[6]<score[7]:
#         result4=data[7]
#     else:
#         result4=data[6]
        
#     result=result1+result2+result3+result4
        
#     return result

# def solution(survey, choices):
#     data = ["R", "T", "C", "F", "J", "M", "A", "N"]
#     score = [0 for str in data]
#     result = ''
    
#     for i in range(len(survey)):
        
#         if 4<choices[i]<=7:
#             score[data.index(survey[i][-1])] += choices[i]-4
#         if choices[i]==4:
#             pass
#         if 1<=choices[i]<4:
#             score[data.index(survey[i][0])] += 4-choices[i]
            
    
#     if score[0]<score[1]:
#         result+=data[1]
#     else:
#         result+=data[0]
        
#     if score[2]<score[3]:
#         result+=data[3]
#     else:
#         result+=data[2]
        
#     if score[4]<score[5]:
#         result+=data[5]
#     else:
#         result+=data[4]
    
#     if score[6]<score[7]:
#         result+=data[7]
#     else:
#         result+=data[6]
        
        
#     return result

def solution(survey, choices):
    data = ["R", "T", "C", "F", "J", "M", "A", "N"]
    score = [0 for str in data]
    result = ''
    
    for i in range(len(survey)):
        
        if 4<choices[i]<=7:
            score[data.index(survey[i][-1])] += choices[i]-4
        if choices[i]==4:
            pass
        if 1<=choices[i]<4:
            score[data.index(survey[i][0])] += 4-choices[i]
            
    for k in range(0,len(score),2) :
        if score[k]<score[k+1]:
            result+=data[k+1]
        else:
            result+=data[k]
            
    return result