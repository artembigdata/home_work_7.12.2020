a = int(input("insert number: "))
max = 0
while a != 0:
 num = a % 10
 if num > max:
  max = num
 a = a // 10
print('maximum digit of a number :' + str(max))








