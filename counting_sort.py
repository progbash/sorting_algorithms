def counting_sort(array, maxvalue):
    length_of_empty_array = maxvalue + 1
    empty_array = [0] * length_of_empty_array

    for element in array:
        empty_array[element] += 1

    index = 0

    for element in range(length_of_empty_array):
        for j in range(empty_array[element]):
            array[index] = element
            index += 1
    return array

mylist = [4, 4, 4, 5, 1, 1, 2, 3, 4, 5]
print(counting_sort(mylist, 5))