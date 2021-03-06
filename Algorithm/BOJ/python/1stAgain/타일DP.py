'''
자. 처음 접근 방식은 
단순한 DP Top-Down 방식이라고 생각할 수 있다.

00 을 선택하는 것은, 2칸 차지하기
1 택하는 것은 1칸 차지하기. 

결국 n 자리수를 2칸, 혹은 1칸 차지하며 올것이냐 
라는 단순한 물음으로 생각할 수 있다.

하지만 ! 
중복 경우가 있음을 잊어서는 안된다

ex. [][][][] 이 있다고 해보자
기존 방식으로 접근하면
[][] 에서
1) 00 붙여서 [][][0][0] 만들기
2) 1 붙여서 [][][][1] 만들기 

더 정확히 예를 들면
0011 이 있을 때,
단순히 1칸 2칸 차지할 것이냐의 관점으로 접근해버리면
1) 001 에서 1 붙이기
2) 00 에서 11 붙이기
가 되버리지만

사실 중복된다
왜냐하면
001 에서 이미
00 에서 1 을 하나 붙이는 경우가 고려되기 때문이다.
즉, N 번째를 고려할 때, i-2번째에서 1을 2번 붙이는 경우는 
중복 우려로 인해 고려하지 않는 것이다.

따라서 우리가 고려할 것은
N 에서의 최대 만들 수 있는 타일 수는
1) N-2 에서 00 붙이기
2) N-1 에서 1 붙이기 이다 

따라서 4자리수라면
1자리 ~ 4자리.
이와 같이 bottom-up 방식으로
dy[n] = dy[n-1] + dy[n-2]를 생각하면 된다.

'''

