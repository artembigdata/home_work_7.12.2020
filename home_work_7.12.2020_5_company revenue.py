a = int(input('enter income Your company: '))
b = int(input('enter expenses Your company: '))
if a > b:
    c = a - b
    print('Your company is profitable.', 'Profit: ', c)
else:
    c = a - b
    print('Your company is not profitable.', 'Loss: ', c)

