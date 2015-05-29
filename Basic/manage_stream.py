__author__ = 'Tong'


# if elif else
#int(input("Please enter an integer: "))
x = 15

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# for
a = ['cat', 'window', 'defenestrate']
for x in a:
    print(x, len(x))

for x in a[1]:
    print(x, len(x))

#range
for i in range(5):
    print(i)

for i in range(len(a)):
    print(a[i])


