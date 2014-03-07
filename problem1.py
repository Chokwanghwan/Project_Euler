#encoding:utf8
'''
프로젝트 오일러 problem1
10보다 작은 자연수 중에서 3 또는 5의 배수는 3,5,6,9 이고, 이것을 모두 더하면 23입니다. 
1000보다 작은 자연수 중에서 3 또는 5의 배수를 모두 더하면 얼마일까요?
'''
result = 0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        result  = result + i
print result

