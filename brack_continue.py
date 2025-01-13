#while loop
x = [1 , 12 ,34 ,54 , 76, 123]

count = 0

# while True:
#     print("Count is",count)
#     count += 1

#     if count == 25:
#         break

#continue

while count == len(x) - 1 :
    print("Index is",count)

    i = x[count]

    if i % 2 == 0:
        count += 1
        continue

    print(i)
    print(i ** 2)
    count += 1