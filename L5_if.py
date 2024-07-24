#if 判斷式
# x = input("Please enter a  number:")       #取得的輸入為字串型式(string)
# #print(type(x))                            #將字串轉為數字型態
# x = int(x)  
# if x>200:
#     print("大於200!")
# elif x>100:
#     print("大於100~小於等於200~200")
# else:
#     print("小於等於100~")   

#ex1. 四則運算
x = int(input("請輸入數字一: "))
y = int(input("請輸入數字二: "))
op = input("請輸入運算+, -, *, / : ")
if op == "+":
    print(x+y)
elif op == "-":
    print(x-y)
elif op == "*":
    print(x*y)
elif op == "/":
    print(x/y)
else:
    print("系統不支援此運算~")