# 순열 크기 상, 다음 크기의 순열을 구하는 코드
# 순열은, 서로 다른 숫자들 끼리의 조합을 이용하여 순서를 정하는 것
# 즉, 중복은 허용되지 않는다

# 다음 크기의 순열을 찾기
def next_permutation(a):
    i = len(a) - 1
    # invere_point를 찾는다
    # 무슨 말이나면, 제일 큰 순열은 뒤로 갈수록 숫자가 작아질 것
    # 다른 말로하면, 앞으로 오면서 숫자가 커질 것
    # 현재 기준, 다음 크기의 순열을 구하기 위해서는
    # 뒤의 숫자보다, 작은 앞의 숫자를 찾고
    # 그 위치를 기준으로 다시 순열을 재정비해야 한다
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    # 이 말은 즉슨, 계속 왼쪽으로 갔다는것
    # 즉, 현재 a로 들어온 순열이 가장 큰 수열에 해당한다는
    if i <= 0:
        return False

    j = len(a) - 1

    # inverespoint를 기준으로, 오른쪽에 있는 숫자중에서
    # inverespoint보다 "한단계" 더 큰 숫자를 찾고 ( 사실 이게 왜 "한단계" 위라고 표현하는지는 잘 모르겠다 )
    # 해당 숫자와 위치를 바꿔준다
    while a[j] <= a[i-1]:
        j -= 1

    a[i-1], a[j] = a[j], a[i-1]

    j = len(a) - 1

    # 그리고, inverse_point에 놓인 새로운 숫자를 기준으로
    # 그 이후의 숫자들을, 오름차순으로, 만들어준다 ( 그래야 다음 크기의 순열이므로 )
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return True
