#1. 有順序可變動列表 List
price = [100, 12, 45, 799, 30]
price[3] = 0        #更改第四筆列表資料:45改為0
price[1:4] = []     #連續刪除列表中從編號1~編號4(不包括)的資料
price[1:4]          #不包含最後一項
price = price + [10, 200, 3000] #列表串接
#print(price)   

length = len(price) #取得列表長度
#print(length)

#2. 巢狀列表
data = [[1, 2, 3], [5, 6, 7, 8]]
#print(data[1][1:3])
data[1][:3] = [0, 0, 0]
#print(data)

#3. 有順序不可變動列表 Tuple
d = (2, 10, 30)
d[1] = 0       #error:Tuple的資料不可變動
print(d)

