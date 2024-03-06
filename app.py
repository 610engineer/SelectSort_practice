def selection_sort(array):
    for i in range(len(array)):
        min:int= i
        for j in range(len(array) - i):
            print("J :",j, array[i+j])
            if array[min] > array[i+j]:
                min = i+j
        print("MIN", array[min])
        array[i], array[min] = array[min], array[i]
        print("ARRAY", array)
    return array
