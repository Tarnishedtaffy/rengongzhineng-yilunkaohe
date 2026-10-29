# 题目：比较月亮大小（1005）
# 分类：语法入门 · 数组、字符串及数据批量存储
# 题目链接：https://ac.nowcoder.com/acm/contest/19306/1005
# TODO: 在下方编写你的代码
import sys
data=sys.stdin.buffer.read().split()
n=int(data[0])
m=list(map(int,data[1:n+1]))
if len(m)==1:
    if m[0]==0:
        print("UP")
    elif m[0]==15:
        print("DOWN")
    else:
        print("-1")
else:
    if m[-1]>m[-2]:
        if m[-1]==15:
            print("DOWN")
        else:
            print("UP")
    elif m[-1]<m[-2]:
        if m[-1]==0:
            print("UP")
        else:
            print("DOWN")
    else:
        print("-1")