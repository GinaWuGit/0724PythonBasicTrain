#1. 隨機模組 Random
#隨機選取
import random
# data = random.choice([11, 2, 55, 65, 17])
# data = random.sample([11, 2, 55, 65, 17], 3)
# print(data)

#隨機調換順序
result = [1, 2, 3, 5, 6, 8]
random.shuffle(result)
print(result)