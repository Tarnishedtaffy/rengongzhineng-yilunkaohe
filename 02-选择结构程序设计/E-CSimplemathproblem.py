# 题目：CSimplemathproblem（E）
# 分类：语法入门 · 选择结构程序设计
# 题目链接：https://ac.nowcoder.com/acm/contest/19304
# TODO: 在下方编写你的代码
X,Y=map(int,input().split())
if Y%X==0:
    print(X+Y)
else:
    print(Y-X)