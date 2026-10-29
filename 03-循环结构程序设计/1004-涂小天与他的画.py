# 题目：涂小天与他的画（1004）
# 分类：语法入门 · 循环结构程序设计
# 题目链接：https://ac.nowcoder.com/acm/contest/19305/1004
# TODO: 在下方编写你的代码
import sys
data = sys.stdin.buffer.read().split()
T = int(data[0])
idx = 1#ai为什么这么喜欢用idx蛤 那我也用
for _ in range(T):
    n = int(data[idx]); idx += 1#这个结构想不到
    mid = n // 2
    for i in range(n):
        d = abs(i - mid)
        print(" " * d + "*" * (n - 2 * d))