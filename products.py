
import os

# 讀取檔案
def read_file(filename):
	x = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if "商品,價格" in line:
				continue
			name, price = line.strip().split(',')
			x.append([name, price])
	return x

# 新增商品
def user_input(products):
	while True:
		name = input("商品名稱：")
		if name == 'q':
			break
		price = input("商品價格：")
		products.append([name, price])
	return products

#列出清單
def print_list(products):
	for p in products: 
		print(p[0], "的價格是", p[1])

# 寫入檔案
def write_file(filename, products):
	with open(filename, 'w') as f:
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')


def main():
	filename = 'products.csv'
	if os.path.isfile(filename):
		products = read_file(filename)
		print(products)
	else:
		print("找不到檔案")

	products = user_input(products)
	print_list(products)
	write_file('products.csv', products)
	print(products)

main()
