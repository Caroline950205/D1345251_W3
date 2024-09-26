a=int(input("請輸入三位數:"))

s=a//100
t=a//10
t2=t%10
l=a%10
f=s+t2+l
print('每位數字的總和:'+str(f))