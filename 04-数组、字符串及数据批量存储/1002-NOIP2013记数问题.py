# 题目：[NOIP2013]记数问题（1002）
# 分类：语法入门 · 数组、字符串及数据批量存储
# 题目链接：https://ac.nowcoder.com/acm/contest/19306/1002
# TODO: 在下方编写你的代码
import sys
data = sys.stdin.buffer.read().split()
n,x = list(map(int,data[0:2]))            # x 保持字符串，不转 int
cnt = 0
for i in range(1, n + 1):
    cnt += str(i).count(f"{x}")   # 数的是变量 x 的字符
print(cnt)