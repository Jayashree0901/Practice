# map function
# t = [3,6,9,2,1,7]
# t1 = list(map(lambda x: x**2, t))
# print(t1)

n1 = [1, 2, 3]
n2 = [4, 5, 6]
n3 = [7, 8, 9]
print(list(map(lambda a,b,c: a+b+c, n1,n2,n3)))

