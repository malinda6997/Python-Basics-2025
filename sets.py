# cantbe duplicate values in a set
#sets are case sensitive
x = {"hellow", "world", "Hellow", "World", "hellow", "malinda"}
y = {"100", "200", "1000"}

z = x.union(y) # or z = x | y
print(z)
