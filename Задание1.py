print("Введите первое число:")       #Задание 1
a = int(input())
print("Введите второе число:")
b = int(input())
if (a < b):
  for i in range(a, b+1):
    print(i, end=" ")
elif (a > b):
  for i1 in range(a, b-1, -1):
    print(i1, end=" ")   
else:
  print("Числа равны")    