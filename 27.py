#Лінійний масив містить відомості про кількість опадів, що випали за кожен з 12 місяців одного року. Складіть програму, що визначає загальну кількість опадів протягом цього року, середньомісячну кількість опадів, кількість посушливих місяців (коли кількість опадів було менше 30 мм), найпосушливіший місяць року.
#Вишневський А.В 122Д
import numpy as np
n = 12
a = np.zeros((n),dtype=int)
sum = 0
count = 0
min = 1000
mid = 0
h = 0
for i in range(n):
    a[i] = int(input(f'Enter your value for {i+1} month'))
    sum += a[i]
    mid += a[i]
    if a[i] <= 30:
        count += 1
    if a[i] < min:
        min = a[i]
        h = i
mid /= 12
print(f'Your arr:{a}\nYour sum:{sum}\nYour middle value:{mid}\nYour count of bad months:{count}')
if h == 0:
    print('January')
elif h == 1:
    print('February')
elif h ==2 :
    print('March')
elif h == 3:
    print('April')
elif h == 4:
    print('May')
elif h == 5:
    print('June')
elif h == 6:
    print('July')
elif h == 7:
    print('August')
elif h == 8:
    print('September')
elif h == 9:
    print('October')
elif h == 10:
    print('November')
elif h == 11:
    print('December')
