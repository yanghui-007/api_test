#range针对数字，如果针对字符，就去掉range

#1.三个1到3进行排列组合：
# for i in range (1,4):
#     for f in range (1,4):
#         for t in range (1,4):
#             print(i,f)

#2.三个1到3进行排列组合，去掉重复数据：
# for i in range (1,4):
#     for k in range (1,4):
#         for j in range (1,4):
#             if(i!=k) and (k!=j) and (i!=j):
#                 print(i,k,j)


#3.兼容性测试，场景进行排列组合：第一种方法，使用range，结合下标
# a=['wap端','微信浏览器']
# b=['QQ浏览器','UC浏览器','chrome','safari']
# c=['礼品卡','steam','游戏代充']
# d=['wifi','4G','3G']
# e=['华为','小米','苹果']

# for i in range (len(a)):
#     for k in range (len(b)):
#         for j in range (len(c)):
#             for t in range (len(d)):
#                 for f in range (len(e)):
#                     #if(i!=k) and (k!=j) and (i!=j):
#                         print(a[i],b[k],c[j],d[t],e[f])


#3.兼容性测试，场景进行排列组合：第二种方法，不使用range，去掉range。g=g+1:用于统计所有排列组合数量
a=['wap端','微信浏览器']
b=['QQ浏览器','UC浏览器','chrome','safari']
c=['礼品卡','steam','游戏代充']
d=['wifi','4G','3G']
e=['华为','小米','苹果']
g=0


for i in a:
    for k in b:
        for j in c:
            for t in d:
                for f in e:
                    #if(i!=k) and (k!=j) and (i!=j):
                        g=g+1
                        print(i,'+',k,'+',j,'+',t,'+',f)
print(g)