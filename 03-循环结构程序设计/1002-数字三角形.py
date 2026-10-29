# 题目：数字三角形（1002）
# 分类：语法入门 · 循环结构程序设计
# 题目链接：https://ac.nowcoder.com/acm/contest/19305/1002
# TODO: 在下方编写你的代码
n=int(input())
k=1
for i in range(1,n+1):
    for j in range(i):
        print(f"{k:4d}",end="")
        k+=1
    print()