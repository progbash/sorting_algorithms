def counting_sort(array, maxvalue):
    length_of_empty_array = maxvalue + 1
    empty_array = [0] * length_of_empty_array

    for element in array:
        empty_array[element] += 1

    # empty_array - her elementden neche denedir. 0-dan bashlayaraq
    print(empty_array)

    index = 0

    for i in range(length_of_empty_array):
        for j in range(empty_array[i]):
            print(f'i {i}')
            array[index] = i
            index += 1
    return array

mylist = [4, 4, 4, 5, 1, 1, 2, 3, 4, 5]
print(counting_sort(mylist, 5))