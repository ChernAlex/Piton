import random
import datetime
import prettytable                  # пакет для таблицы
import matplotlib.pyplot as plt     # библиотека для графика

def BubbleSort(A):                  # сортировка пузырьком
    for i in range(len(A)):
        for j in range(len(A)-1-i):
            if A[j] > A[j+1]:
                a = A[j]
                A[j] = A[j+1]
                A[j+1] = a

"""4. Функция сортировки вставками insert:
Цикл 1 – по i от 1 до N :					# i - текущая позиция при проходе по списку
	Действие – сохранение t = A[i]		# A[i] - вставляемый элемент
	Действие – новая  переменная j = i 	# j - позиция в отсортированной части списка
	Цикл 2 – по j до 0 с шагом -1 :		# j - смещается справа налево, от больших к меньшим
		Условие если A[j-1]>t : 			# эл-ты отсортированной части, большие вставляемого
			Действие – A[j] = A[j-1] 		# уступают место – сдвигаются (копируются) вправо
		Иначе – выход из цикла 2		# j остановится на посл. эл-те, большем вставляемого
		Действие – A[j] = t				# вставляемый эл-т ставится на освободившееся место"""

def insertion(A):          # сортировка вставками
	for i in range(len(A)):
		j = i - 1
		key = A[i]
		while A[j] > key and j >= 0:
			A[j + 1] = A[j]
			j -= 1
		A[j + 1] = key
	return A


"""def QuickSort(A, fst, lst):         # быстрая сортировка
    if fst >= lst:
        return

    #i, j = fst, lst
    pivot = A[fst]
    # pivot = A[random.randint(fst, lst)]
    first_bigger = fst+1
    while first_bigger <= lst:
        if A[first_bigger] >= pivot:
            break
        first_bigger += 1
    i = first_bigger+1
    while i <= lst:
        if A[i] < pivot:
            A[i], A[first_bigger] = A[first_bigger], A[i]
            first_bigger += 1
        i += 1

    last_smaller = first_bigger-1
    A[fst], A[last_smaller] = A[last_smaller], A[fst]
    QuickSort(A, fst, last_smaller-1)
    QuickSort(A, first_bigger, lst)"""


table = prettytable.PrettyTable(["Размер списка", "Время пузырька", "Время вставками"])
x=[]
y1=[]
y2=[]



for N in range(1000,5001,1000):
    x.append(N)
    min=1
    max=N
    A=[]
    for i in range (N):
        A.append(int(round(random.random()*(max-min)+min)))

    #print(A)

    B = A.copy()
    # print(B)

    # BubbleSort(A)
    print("---")
    # print(A)


    # QuickSort(B, 0, len(B)-1)
    print("---")
    # print(B)

    t1 = datetime.datetime.now()
    BubbleSort(A)
    t2 = datetime.datetime.now()
    y1.append((t2-t1).total_seconds())
    print("Пузырьковая сортировка   " +str(N)+"   заняла   "+str((t2-t1).total_seconds()) + "c")

    t3 = datetime.datetime.now()
    insertion(B)
    t4 = datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    print("Вставками   " +str(N)+"   заняла   "+str((t4-t3).total_seconds()) + "c")

    table.add_row([str(N), str((t2-t1).total_seconds()), str((t4-t3).total_seconds())])
print(table)

plt.plot(x, y1, "C0")
plt.plot(x, y2, "#F3FF80")
plt.show()