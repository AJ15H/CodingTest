def solution(phone_number):
    count = len(phone_number)
    n = phone_number.replace(phone_number[:-4], '*'*(count-4)
                            )   

        
    
    return n