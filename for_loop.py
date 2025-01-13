x = [1 , 12 ,34 ,54 , 76, 123]

# for i in enumerate(x):
#     print(i)

# for index, value in enumerate(x):
#     print(index , value)

# for i in range(0, 10):
#     print(i)

# r = range(0, 10)
# print(type(r))
# for i in r:
#     print(i)

r = range(0, len(x))
print(type(r))
for i in r:
    print(x[i])