def bubble_sort(array):
    length = len(array)
    for i in range((length-1), 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array

mylist = [5,4,6,1,2]
print(bubble_sort(mylist))