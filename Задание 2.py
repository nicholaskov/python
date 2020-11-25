print("Введите первое 4-х значное число:") #задание 2
a=int(input())
print("Введите второе 4-х значное число:")
b=int(input())
for i in range(a, b+1):
    s=str(i)
    n=str(i)[::-1]
    if s == n:
        print(s)