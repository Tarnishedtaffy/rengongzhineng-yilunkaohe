# 题目：箭形图案（1005）
# 分类：语法入门 · 循环结构程序设计
# 题目链接：https://ac.nowcoder.com/acm/contest/19305/1005
# TODO: 在下方编写你的代码
# def func():
#     import sys
#     data=sys.stdin.buffer.read().split()
#     a=int(data[0])
#     #a=int,sys.stdin.read().split() 好像不能这样写
#     #第一个a*2*2*" 后续a-i " 最多*是a+1个
#     for i in range(a+1):
#         print((a-i)*2*" "+(1+i)*"*")
#     for i in range(a-1,-1,-1):
#         print((a-i)*2*" "+(1+i)*"*")
# func()
import sys

# 多组输入：一行一个整数，读到文件结束自动停
for line in sys.stdin:
    n = int(line)

    # 上半段（含最长那一行）：星号 1,2,...,n+1，缩进每行少 2 个空格
    for i in range(n + 1):
        print(" " * (2 * (n - i)) + "*" * (i + 1))

    # 下半段：星号 n,n-1,...,1，缩进每行多 2 个空格
    for i in range(n - 1, -1, -1):
        print(" " * (2 * (n - i)) + "*" * (i + 1))
