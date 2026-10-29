# 题目：233（1005）
# 分类：语法入门 · 函数与递归
# 题目链接：https://ac.nowcoder.com/acm/contest/19859/1005
# TODO: 在下方编写你的代码
# import sys
# data=sys.stdin.buffer.read().split()
# t=int(data[0])
# n=list(map(int,data[1:t*2+1]))
# for i in range(1,t+1):
#     print(f"{int(data[i*2])*int(data[i*2+1])}")
import sys
data = sys.stdin.buffer.read().split()
t = int(data[0])
for i in range(t):
    print(int(data[1 + i*2]) * int(data[1 + i*2 + 1]))
