def dfs(depth, num, numbers, target, arr):
    if depth >= len(numbers):  # 모든 값 계산 했을 경우
        if target == num:
            arr.append(1)   # 결과값이 만족할 경우 arr에 1 삽입
        return
    dfs(depth + 1, num + numbers[depth], numbers, target, arr)
    dfs(depth + 1, num - numbers[depth], numbers, target, arr)
    # depth = numbers의 index
    # num= 순차적으로 값을 더하거나 뺀값
    # numbers 계산할 값들 [4, 1, 2, 1]
    # target 결과값
    # arr 만족하는 경우에 1 넣기
def solution(numbers, target):
    arr = []
    dfs(0, 0, numbers, target, arr)
    answer = len(arr)   # arr에 만족하는 경우 만큼 1 들어감
    return answer