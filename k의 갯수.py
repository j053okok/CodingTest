def solution(i, j, k):
    answer = 0
    x = [i for i in range(i, j + 1)]
    for num in x:
        for a in str(num):
            if a == str(k):
                answer += 1
    return answer


print(solution(1, 13, 1))
print(solution(10, 50, 5))
print(solution(3, 10 ,2))
# https://school.programmers.co.kr/learn/courses/30/lessons/120887