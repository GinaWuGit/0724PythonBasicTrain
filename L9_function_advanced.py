#1. 函式接受無限參數
# def say(*msg):
#     for x in msg:
#         print(x)

# say("Gina", "Julia", "Eric") 

#2. 參數的預設資料
# def power(base, exp=0):     #給定預設值
#     print(base**exp)

# power(4, 3)
# power(6)    

#3. 使用參數名稱對應
# def divide(a, b):
#     print(a/b)

# divide(b=64, a=16)
# divide(6,3)

#4. 無限 / 不定長度參數資料
def average(*n):
    sum = 0
    for i in n:
        sum += i
    print(sum/len(n))

average(1, 3, 5, 7)
average(1, -10, 5, 7, -100, 12)
