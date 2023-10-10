def solution(sides):
    a=max(sides)
    sides.remove(a)
    if a<sum(sides):
        return 1
    else:
        return 2