# 题目：比大小（A）
# 分类：语法入门 · 选择结构程序设计
# 题目链接：https://ac.nowcoder.com/acm/contest/19304
# TODO: 在下方编写你的代码
a,b=list(map(int,input().split()))
if a<b:
    print("<")
elif a==b:
    print("=")
else:
    print(">")