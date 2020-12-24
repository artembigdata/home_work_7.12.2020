a = int(input("enter time second: "))
hour = a // 3600
minutes = a % 3600 // 60
seconds = a % 3600 % 60
print(f"{hour}:{minutes}:{seconds}")








