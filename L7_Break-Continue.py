#1. break 範例
# n = 0
# while n < 5:
#     if n == 3:
#         break
#     print(n)
#     n += 1
# print("最後的n:", n)

#2. continue 範例
# n = 0
# for x in range(9):
#     if x%2 == 0:        #判斷x是否為偶數
#         continue
#     print(x)
#     n += 1
# print("總奇數個數:", n)

#3. ex:找出整數平方根(if -else)
x = int(input("請輸入一整數: "))
for i in range(x):      #i從 0 ~ x-1
    if i*i == x:
        print("此數平方根為:", i)
        break           #用 break 強制結束迴圈時，不會執行else
else:
    print("此數非平方數!")


