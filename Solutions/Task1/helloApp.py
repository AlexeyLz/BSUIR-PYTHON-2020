import sys
import argparse

nums = [0,2,1,5,120,-4]


def task_second(finalDicionary):
   listd=list(finalDicionary.items())
   listd.sort(key=lambda i: -i[1])
   finalDict = dict(listd)
   temp = list(finalDict.keys())
   i =0
   print("Предложение:")
   return temp;


def printer(finalDictionary):
   print("Повторения всех слов: ")
   for key in finalDictionary:
       print(key, finalDictionary[key])

   print("---------------------------")


def partition(nums, low, high):
    # Выбираем средний элемент в качестве опорного
    # Также возможен выбор первого, последнего
    # или произвольного элементов в качестве опорного
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # Если элемент с индексом i (слева от опорного) больше, чем
        # элемент с индексом j (справа от опорного), меняем их местами
        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):
    # Создадим вспомогательную функцию, которая вызывается рекурсивно
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)

def input_sort(path):
    with open(path, 'r') as f_obj:
        line = f_obj.read()

    l = len(line)
    integ = []
    i = 0
    while i < l:
        s_int = ''
        a = line[i]
        while '0' <= a <= '9':
            s_int += a
            i += 1
            if i < l:
                a = line[i]
            else:
                break
        i += 1
        if s_int != '':
            integ.append(int(s_int))

    return integ

def merge_sort(alist):

    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    return alist


def task_three(path):
    nums = input_sort(path)
    quick_sort(nums)
    print(nums)
    return 0

def task_four(path):
    print(merge_sort(input_sort(path)))
    return 0

def fibo(path):
    fib1 = 1
    fib2 = 1
    with open(path, 'r') as f_obj:
        n = f_obj.read()

   # n = input("Введите n: ")
    n = int(n)
    print("1 1", end=' ')
    i = 0
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
        print(fib2, end = ' ')




def task_first(path):
  #line = input("Ввведите строку: ")

  with open(path, 'r') as f_obj:
      line = f_obj.read()
  print("Исходная строка: ", line)
  dictionary = dict()
  dictionary = line.split(' ')
  finalDictionary = dict()
  #print(dictionary)
  i = 0
  j = 0

  while i < len(dictionary):
      counter = 0
      j = 0
      while j < len(dictionary):
          if dictionary[i] == dictionary[j]:
              counter += 1
          j+=1
     # print(dictionary[i] + " " + str(counter))
      finalDictionary[dictionary[i]] = counter
      i=i+1

  printer(finalDictionary)
  sentence = task_second(finalDictionary)
  print(' '.join(sentence))


def chosing_task(task_num, path):

    if task_num.lower() == "task12" or task_num.lower() == "task1" or task_num.lower() == "task2":
        task_first(path)
    elif task_num.lower() == "task3" or task_num.lower() == "task3":
        task_three(path)
    elif task_num.lower() == "task4":
        task_four(path)
    elif task_num.lower() == "dop1":
        fibo(path)
    else: print("kek")



def create_parser():

    parser = argparse.ArgumentParser(description='task, path')
    parser.add_argument('task', type=str, help='Input dir for videos')
    parser.add_argument('path', type=str, help='Output dir for image', default='none')

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    parser = create_parser()




print('\n')
if parser.task == "null" or parser.path == 'null':
    print("Повторите ввод!")
    print("Номера заданий: \n 1)task12\n 2)task12 \n 3)task3 \n 4)task4 \n dop1 \n dop2")
else:
    print("Задание: {}".format(parser.task))
    chosing_task(format(parser.task), format(parser.path))