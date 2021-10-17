import random


can_draw_times = int(input("請輸入您消費的金額：")) // 500  # 可以抽獎幾次
drawed_num = []  # 存已經抽到的數字
drawed_str = ''

# 開始抽獎
for i in range(can_draw_times):
	drawed_num.append(drawed := random.randint(0,9))
	drawed_str = drawed_str + str(drawed)
	
	if drawed_str.find('2022') != -1:  # 頭獎
		print("You are the lucky guy!")
		break
	elif drawed_num.count(2) >= 3 and drawed_num.count(0) >= 1:  # 二獎
		print("You win the second prize")
		break

print("Draw end!")
