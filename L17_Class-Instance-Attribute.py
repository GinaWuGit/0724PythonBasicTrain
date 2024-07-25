#1. Point 實體物件設計: 座標平面上的點
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     #定義實體方法
#     def show(self):
#         print(self.x, self.y)
#     def distance(self, targetx, targety):
#         return (((self.x-targetx)**2)+((self.y-targety)**2))**0.5
# p1 = Point(100, 20)
# p1.show()       #呼叫實體方法(本質為一函式))
# p2 = Point(5, 12)
# p2.show()
# result = p2.distance(0, 0)      #計算(5, 12)到(0, 0)之間的距離
# print(result)

#2. Fullname 實體物件設計:包裝檔案讀取
class File:
    # 初始化函式l
    def __init__(self, name):
        self.name = name
        self.file = None    #尚未讀取檔案所以為None
    # 實體方法
    def open(self):
        self.file = open(self.name, mode = "r", encoding = "utf-8")
    def read(self):
        return self.file.read()
#讀取第一個檔案
f1 = File("data1.txt")
f1.open()   #呼叫實體方法
result1 = f1.read()
print(result1)
#讀取第二個檔案
f2 = File("data2.txt")
f2.open()
result2 = f2.read()
print(result2)