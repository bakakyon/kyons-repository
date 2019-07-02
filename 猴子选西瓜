'''
有一堆西瓜，每个西瓜的重量都为整数且重量都不一样，
现在有一猴子可以从这对西瓜中选择拿去若干个西瓜，问猴子有多少中选法？
（将每种选法打印出来）
'''
print("猴子选西瓜")

n=int(input("请输入西瓜总数：\n"))


xg=list(range(1,n+1))
print(xg)

nf=[]
z=[]


   
def nafa(a,b,c):#a=循环初始值 b=循环结束值 c=列表长度
   global nf
   global z
   if c<1:
      return
   else:
      for i in range(a,b):
         nf.append(i)
         nafa(i+1,b+1,c-1)
         if c==1:
            temp=nf[:]
            z.append(temp)
         nf.remove(i)

   
for i in xg:
   nafa(1,n-i+2,i)

print(z)
print("一共"+str(len(z))+"种")
