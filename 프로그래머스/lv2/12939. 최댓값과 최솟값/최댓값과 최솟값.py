def solution(s):
    s_list = s.split(" ")
    n_list = list(map(int,s_list))
    data =f'{min(n_list)} { max(n_list)}'
    
    return data
    # print(f'min(n_list), max(n_list)')
    # data = s.split(" ")
    # print(data)
    