# #1. Point 實體物件設計: 座標平面上的點
# class Point:
#     def __init__(self, x, y):
#         self.x=x        #實體屬性1
#         self.y=y        #實體屬性2
# #建立第一實體物件
# p1 = Point(11, 22)           
# print(p1.x, p1.y)
# #建立第二實體物件
# p2 = Point(33, 44)
# print(p2.x, p2.y)

#2. Fullname 實體物件設計:分開紀錄姓、名的全名
class Fullname:
    def __init__(self, first, last):
        self.first = first
        self.last = last
# 建立第一姓名
name1 = Fullname("Gina", "Wu")
print(name1.first, name1.last)      #操作實體物件屬性
# 建立第二姓名
name2 = Fullname("Alex", "Wang")
print(name2.first, name2.last)