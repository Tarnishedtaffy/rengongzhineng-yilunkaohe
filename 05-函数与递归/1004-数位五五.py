# 题目：数位五五（1004）
# 分类：语法入门 · 函数与递归
# 题目链接：https://ac.nowcoder.com/acm/contest/19859/1004
# TODO: 在下方编写你的代码
a,b=list(map(int,input().split()))
n=0
for i in range(a,b+1):
    if sum(list(map(int,str(i))))>=5 and sum(list(map(int,str(i))))%5==0:
        n+=1
print(n)