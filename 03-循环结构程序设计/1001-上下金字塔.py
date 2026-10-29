# 题目：上下金字塔（1001）
# 分类：语法入门 · 循环结构程序设计
# 题目链接：https://ac.nowcoder.com/acm/contest/19305/1001
# TODO: 在下方编写你的代码
import sys
for i in sys.stdin.buffer.read().split():
    n=int(i)
    for i in range(n):
        print(' ' * (n - 1 - i) + '*' * (2 * i + 1))
    for i in range(n-2,-1,-1):
        print(' ' * (n - 1 - i) + '*' * (2 * i + 1))