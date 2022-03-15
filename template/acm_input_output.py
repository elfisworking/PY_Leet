
#case 1 : 有多组输入数据，但没有具体的告诉你有多少组，只是让你对应每组输入，应该怎样输出？
while True:
    a, b = map(int, input().strip().split())
    print(a, b)
    break

#case 2 : 输入一个整数，告诉我们接下来有多少组数据，然后在输入每组数据的具体值
cases = input().strip()
for i in range(cases):
    a, b = map(int, input().strip().split())

#case 3 : 有多组输入数据，没有具体的告诉你有多少组，但是题目却告诉你遇见什么结束
while True:
    a, b = map(int, input().strip().split())
    if a == 0 and b == 0:
        break
#case 4 : 输入有多组，并却题目告诉你每组输入遇见什么结束，与第三种不同之处在于，每组输入都有相应的细化。
cases = input().strip()
for i in range(cases):
    a, b = map(int, input().strip().split())
    if a == 0 and b == 0:
        break
#case 5 : 这次的输入实现输入一个整数，告诉我们有多少行，在输入每一行。对于每一行的输入，有划分为第一个数和其他的数，第一个数代表那一组数据一共有多少输入。
tcase = int(input().strip())
for case in range(tcase):
    data = map(int, input().strip().split())
    n, array = data[0], data[1:]    
    sum = 0
    for i in range(n):
        sum += array[i]

#case 6 : print 输出不换行
print("test", end="")