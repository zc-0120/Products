products = []
import os

# 讀取檔案
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		name = line.strip().split(',')[0]
		price = line.strip().split(',')[1]
		products.append([name, price])

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

# 寫入檔案
with open('products.csv', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')