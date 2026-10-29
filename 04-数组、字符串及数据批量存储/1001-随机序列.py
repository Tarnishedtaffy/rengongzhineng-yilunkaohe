# 题目：随机序列（1001）
# 分类：语法入门 · 数组、字符串及数据批量存储
# 题目链接：https://ac.nowcoder.com/acm/contest/19306/1001
# TODO: 在下方编写你的代码
# import sys
# t=int(input())
# for i in range(1,t+1):
#     n=int(input())
#     m=list(map(int,sys.stdin.buffer.readline().split()))
#     a=max(m)-min(m)
#     b=sum(m)/n
#     cnt=0
#     for j in range(n):
#         cnt+=(m[j]-b)**2
#     print(f"{a} {cnt/n:.3f}")
import sys
read = sys.stdin.buffer.readline

t = int(read())
for i in range(t):
    n = int(read())
    m = list(map(int, read().split()))
    a = max(m) - min(m)
    b = sum(m) / n
    cnt = 0
    for j in range(n):        # 下标 0 到 n-1
        cnt += (m[j] - b) ** 2
    print(f"{a} {cnt/n:.3f}")