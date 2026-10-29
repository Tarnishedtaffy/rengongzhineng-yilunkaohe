# 题目：[NOIP2010]数字统计（1001）
# 分类：语法入门 · 函数与递归
# 题目链接：https://ac.nowcoder.com/acm/contest/19859/1001
# TODO: 在下方编写你的代码
r,l=list(map(int,input().split()))
n=0
for i in range(r,l+1):
    n+=str(i).count('2')
print(n)