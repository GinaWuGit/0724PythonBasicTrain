#數字運算
x = 9**0.5      #開根號
x += 1
x -= 3          #x = x - 3
y = 5/2         #小數除法
z = 7//6        #整數除法
k = 11%3        #取餘數(mod)
#print(x, y, z, k)

#字串運算
#字串會對內部的字元編號(索引)，從0開始編號
s= "NCUgirl"       #字串以單雙引號表示皆可
s1 = 'EE\n'
s2 = "practice\"ing"      #\:跳脫字元
s3 = "Hello" + "world\n"  #字串串接
s4 = "Hello" "world"
s5 = "Great"*3 + "job"*2
print(s, s1, s2, s3, s4, s5)
print(s[3:6])       #[x, y]:包含開頭不包含結尾
print(s[3:])
print(s[:6])