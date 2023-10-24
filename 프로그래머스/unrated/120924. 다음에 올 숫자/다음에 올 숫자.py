def solution(common):
    # 등차 수열
    if common[1]-common[0]==common[2]-common[1]:
        diff=common[1]-common[0]
        return common[-1]+diff
    # 등비 수열
    else:
        diff=common[1]//common[0]
        return common[-1]*diff