#1. 集合 Set
s1 = {10, 30, 66}
# print(10 not in s1)
# print(11 not in s1)

s2 = {30, 5, 88, 1}
s3 = {1, 3, 5}
s4 = s2 & s3
s5 = s2 | s3       #聯集:取兩集合中所有資料，但不重複取
s6 = s2 - s3       #從s2中減去與s3重疊部分
s7 = s2 ^ s3       #反交集:取兩集合中，不重疊的部分
# print(s7)

s = set("bridges")
# print(s)
# print("g" in s)

#2. 字典:key-value配對
dic = {"blue":"藍色", "pink":"粉紅"}
dic["pink"] = "顏色"
# print(dic["pink"])
# print("blue" in dic)   #以key為主

del dic["pink"]          #刪除字典中鍵值對(key-value pair)
# print(dic)

dic1 = {x:x*2 for x in [10, 20, 30]}    #從列表資料為基礎產生字典
print(dic1)