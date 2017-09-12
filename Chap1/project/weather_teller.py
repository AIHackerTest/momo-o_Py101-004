from sys import argv

script,filename=argv

weather_dict={}

with open(filename) as f:
	for line in f:
		a=line.split(',')
		weather_dict[a[0]]=a[1]

history={}

while True:
	city=input('请输入你想查询天气的城市：')

	if city in weather_dict.keys():
		weather=weather_dict[city]
		print(weather)
		history[city]=weather

	elif city=="help":
		print('\t输入中国县级市以上地区名，查询该地区天气；\n\t输入"help"，查询帮助文档；\n\t输入"history",查看历史查询记录;\n\t输入"quit",退出程序并打印此次查询记录')

	elif city=="history":
		print("你的查询历史为:\n")
		for city in history:
			print(city+":"+history[city])

	elif city=="quit":
		print("你的查询历史为:")
		for city in history:
			print(city+":"+history[city])
		print("\n感谢使用本次服务!")
		exit(0)
		break
	else:
		print('请输入正确的城市名。')


