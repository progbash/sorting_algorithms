def selection_sort(array):
    last_index = len(array) - 1

    for index in range(last_index, 0, -1):
        indexOfMaxValue = 0

        # here i find max value
        for location in range(1, index+1):
            if array[location] > array[indexOfMaxValue]:
                indexOfMaxValue = location
        
        temporary = array[index]
        array[index] = array[indexOfMaxValue]
        array[indexOfMaxValue] = temporary
    
    return array

mylist = [3, 5, 7, 1, 2, 8, 12]
print(selection_sort(mylist))