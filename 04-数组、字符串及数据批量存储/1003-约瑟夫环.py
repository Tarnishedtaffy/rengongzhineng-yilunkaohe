# 题目：约瑟夫环（1003）
# 分类：语法入门 · 数组、字符串及数据批量存储
# 题目链接：https://ac.nowcoder.com/acm/contest/19306/1003
# TODO: 在下方编写你的代码
import sys
data=sys.stdin.buffer.read().split()
n,k,m=list(map(int,data[0:3]))
p= list(range(n))
x=k
while len(p)>1:
    x=(x+m-1)%len(p)
    p.pop(x)
a=int(p[0])
print(a)