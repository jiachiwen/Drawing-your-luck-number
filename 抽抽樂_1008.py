#消費者輸入自己消費的金額，每達500則可獲得增加隨機抽取數字的機會，舉例：500可抽1數字，2000可抽4數字
# 消費者隨機抽數字
#3個2，1個0，即可開二獎；若完整抽到2022字樣，則得頭獎

ml=[]
import random
w=0
u=0

print("請輸入您消費的金額：")
a=int(input())
s=a//500

for b in range(1,s+1):
    while len(ml)<s:
        x=random.randint(0,9)
        ml.append(x)
        if x==2:
            w+=1
            continue
        elif x==0:
            u+=1
            continue
        else:
            continue

print("w=",w)
print("u=",u)
print(ml)
if w>=3 and u>=1:
    print("You win the second prize")
elif ml==[2,0,2,2]:
    print("You are the lucky guy!")
else:
    print("Try again!")
