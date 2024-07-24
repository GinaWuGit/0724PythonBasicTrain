#1. 定義函式
# #函式內部程式碼若無函式呼叫，就不會執行
# def multiply(x, y):
#     print(x*y)
#     return x*y

# #呼叫函式
# multiply(2, 5)
# multiply(11, 3)
# value = multiply(7, 3) + multiply(1, 1)
# print(value)

#2. 程式包裝(1~n的和):函式可用來做成式包裝，同樣邏輯可重複利用
def calculate(x):
    sum = 0
    for x in range (x+1):
        sum += x
    print(sum)

calculate(10)
calculate(100)