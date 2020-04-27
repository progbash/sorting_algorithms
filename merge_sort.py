def merge_sort(array):
    length = len(array)
    middle_index = length//2

    if length > 1:
        lefthalf = array[:middle_index]
        righthalf = array[middle_index:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                array[k] = lefthalf[i]
                i += 1
            else:
                array[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            array[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            array[k] = righthalf[j]
            j += 1
            k += 1 

    return array

mylist = [1,6,3,8,2,5,4]
print(merge_sort(mylist))