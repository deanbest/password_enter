# 數值, 答案的東西存一次就好
# 才不會之後要改的話, 多個地方要改

password = 'a123456'
y = 3  # 剩餘機會
while True:
	code = input('請輸入密碼: ')
	if code == password:
		print('登入成功!')
		break
	else:
		y = y - 1
		if y == 0:
			break
		print('密碼錯誤, 還有', y, '次機會') 
		


