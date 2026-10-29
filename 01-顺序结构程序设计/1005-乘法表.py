# 题目：乘法表（1005）
# 分类：语法入门 · 顺序结构程序设计
# 题目链接：https://ac.nowcoder.com/acm/contest/18839/1005
# TODO: 在下方编写你的代码
out = []
for i in range(1, 10):          # i = 1 到 9，表示第 i 行
        row = []
        for j in range(1, i + 1):   # j = 1 到 i
            row.append(f"{j}*{i}={j*i:2}")   # 结果占2字符宽
        out.append(" ".join(row))   # 每项之间用一个空格连起来
print("\n".join(out))  