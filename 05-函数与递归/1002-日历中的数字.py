# 题目：日历中的数字（1002）
# 分类：语法入门 · 函数与递归
# 题目链接：https://ac.nowcoder.com/acm/contest/19859/1002
# TODO: 在下方编写你的代码
import sys
import calendar
for s in sys.stdin:
    if not s.strip():#即if s.strip() == "":
        continue# s 含行末的 "\n"。若整行只有空白，strip() 后得到空串
    y,m,x=s.split()
    y,m=int(y),int(m)
    n=calendar.monthrange(y,m)[1]#取天数
    print(sum(("%d-%02d-%02d" % (y, m, d)).count(x) for d in range(1, n + 1)))