# 题目：字符金字塔（1003）
# 分类：语法入门 · 循环结构程序设计
# 题目链接：https://ac.nowcoder.com/acm/contest/19305/1003
# TODO: 在下方编写你的代码
c = input().strip()
n = ord(c) - ord('A') + 1
for i in range(n):
    up = ''.join(chr(ord('A') + k) for k in range(i + 1))
    down = ''.join(chr(ord('A') + k) for k in range(i - 1, -1, -1))
    print(' ' * (n - 1 - i) + up + down)
