n=int(input("请输入一共有多少人：\n"))
a=list(range(1,n+1))

i=0
while n>1:
   for j in range(1,4):
      if i==len(a):
         i=0
      if j==3:
         del a[i]
         i-=1
         n-=1
      i+=1

print(a)      
