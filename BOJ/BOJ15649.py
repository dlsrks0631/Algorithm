'''
BOJ 15649. N과 M

자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램
-> 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

< 아이디어 >
-> 백트래킹 재귀함수 안에서, for 돌면서 숫자 선택 (방문 여부 확인)
-> 재귀함수에서 M개를 선택할 경우 print

< 시간복잡도 >
-> N! ->

< 자료구조 >
-> 결과값 저장
-> 방문여부 체크
'''
import sys

input = sys.stdin.readline

n,m = map(int,input().split())
result = [] # 결과값
check = [False] * (n+1) # 방문여부

def recursive(num):
    if num == m:
        # print(' '.join(map(str, result))) # result값을 string으로 바꿔줌
        print(result)
        return
    for i in range(1,n+1):
        if check[i] == False:
            check[i] = True
            result.append(i)
            recursive(num+1)
            # check[i] = False
            # result.pop()

recursive(0)
