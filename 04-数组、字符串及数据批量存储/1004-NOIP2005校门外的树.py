# 题目：[NOIP2005]校门外的树（1004）
# 分类：语法入门 · 数组、字符串及数据批量存储
# 题目链接：https://ac.nowcoder.com/acm/contest/19306/1004
# TODO: 在下方编写你的代码
# import sys #做一个[]把m都放进去 把里面的数字个数求出来 减去l
# data=sys.stdin.buffer.read().split()
# 
# M=[]
# for i in range(m):
#     M.append(tuple(range(list(map(int,data[i*2,i*2+2])))))
import sys
data=sys.stdin.buffer.read().split()
L,M=list(map(int,data[:2]))
i=2
tree=[1]*(L+1)
for _ in range(M):
    l,m=list(map(int,data[i:i+2]))
    i += 2                             # 移到下一个区间
    for j in range(l, m + 1):            # r+1 才包含右端点
        tree[j] = 0  
print(sum(tree))