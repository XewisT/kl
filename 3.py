# Створіть масив з п'яти прізвищ і виведіть їх на екран стовпчиком, починаючи з останнього.
#Вишневський А.В 122Д
n = 5
a = []
for i in range (n):
   a.append(input(f'Введите {i+1} фамилию'))
k = a[::-1]
for i in k :
    print(i)
