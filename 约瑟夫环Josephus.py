
# coding=utf-8
#Coded By CWhide
#20240211

#过程版本
#约瑟夫圆逆时针排序
#Josephus

n = int(input("输入约瑟夫环的元素个数"))
k=1
m=0
for i in range(1,int(n**0.5+1)+1):
    if 2**i<n<2**(i+1): #此时i为符合条件的最小的2次方
        m=1
        for j in range(2**i,n):
            k+=2
        print("第",k,"个元素存活"," ",k,"is survival")
        break
if m!=1:
    print("第一个元素存活  The first number is survival")

       