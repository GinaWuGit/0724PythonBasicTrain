#1. 儲存 / 寫入檔案
# file = open("demo.txt", mode = "w", encoding = "utf-8")     #開啟檔案
# file.write("Keep going for python!\nThere are three tutor today~\n測試中文")    #操作檔案
# file.close() 

# file = open("demo.txt", mode = "w", encoding = "utf-8")     #開啟檔案
# file.write("20\n40\n60")    #操作檔案
# file.close() 

# file1 = open("demo.py", mode = "w")     #開啟檔案
# file1.write("print Gina")    #操作檔案
# file1.close() 

#2. 讀取檔案
# with open("L3_List-Tuple.py", mode = "r", encoding = "utf-8") as file:
#     data = file.read()
# print(data)

#EX:把檔案中數字資料逐一讀取出來，並計算總合
# sum = 0
# with open("demo.txt", mode = "r", encoding = "utf-8") as file:
#     for line in file:       #一行一行讀取
#         sum += int(line)
# print(sum)

#3. 讀取檔案
import json
with open("config.json", mode = "r") as file:
    data = json.load(file)
data["name"] = "New name"       #修改變數資料
print(data)     #是一字典
#把最新資料複寫進檔案
with open("config.json", mode = "w") as file:
    json.dump(data, file)
# print("name:", data["name"])
# print("version", data["version"])
