#內建模組
import sys 

# print(sys.platform)
# print(sys.maxsize)
# print(sys.path)

#建立geometry module並載入使用(自定義模組)
# import geometry
# result = geometry.distance(1, 1, 5, 5)
# print(result)
# result = geometry.slope(1, 3, 5, 11)
# print(result)

#3. 調整搜尋路徑(模組的搜尋中不包含自行創建的資料夾)
sys.path.append("modules")      #在模組搜尋路徑列表中【新增路徑】
print(sys.path)
import geometry
result = geometry.slope(1, 3, 5, 11)
print(result)