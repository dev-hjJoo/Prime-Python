
# 코드 3-28 : 사용자로부터 입력을 받은 후 누적 합계 값 구하기


n = int(input('합계를 구할 수를 입력하세요 : '))
s = 0


for i in range(0, n) :
    s = s + (i+1)

print('1부터 {}까지의 합은 {}'.format(n, s))