# 题目：素数回文（1003）
# 分类：语法入门 · 函数与递归
# 题目链接：https://ac.nowcoder.com/acm/contest/19859/1003
# TODO: 在下方编写你的代码
t=input()
a=int(t+t[:-1][::-1])
def func(x):
    if x<2:
        return False
    if x%2==0:
        return x==0
    i=3
    while i*i<=x:
        if x%i==0:
            return False
        i+=2
    return True
print("prime" if func(a) else "noprime")