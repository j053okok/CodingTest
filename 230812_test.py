def solution(n):
    x, y = 0, 1
    a = [1]
    while len(a) < n:
        z = x + y
        a.append(z)
        x, y = y, z
    return a


print(solution(10))