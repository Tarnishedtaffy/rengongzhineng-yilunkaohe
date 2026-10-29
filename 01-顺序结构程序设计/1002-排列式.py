# 题目：排列式（1002）
# 分类：语法入门 · 顺序结构程序设计
# 题目链接：https://ac.nowcoder.com/acm/contest/18839/1002
# TODO: 在下方编写你的代码
num=[]
for i in range(1,10000):
    for j in range(i,10000):
            p=i*j
            if p>9999:
                break
            s=str(p)+str(i)+str(j)
            if sorted(s)==sorted('123456789'):
                num.append((p,i,j))
num.sort()
for p,i,j in num:
    print('%d = %d x %d'%(p,i,j))