products = []

# 新增商品
while True:
	name = input("商品名稱：")
	if name == 'q':
		break
	price = input("商品價格：")
	products.append([name, price])
print(products)

#列出清單
for p in products: 
	print(p[0], "的價格是", p[1])