#def selectionSort(arr):
#    for i in range(len(arr)):
#        min = float('-inf')
#        for j in range(i + 1, len(arr)):
#            if arr[i] > arr[j]:
#                arr[i],arr[j] = arr[j], arr[i]
#    return arr
    
#print(selectionSort([89,56,45,34,65,76]))

def selectionSort(arr):
    for i in range(len(arr)):
        # Assume the current element is the minimum
        min_index = i
        for j in range(i + 1, len(arr)):
            # Find the index of the minimum element in the remaining unsorted part
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

#print(selectionSort([89,56,45,34,65,76]))                      for inbuilt input

# Take input from the user
n = int(input("Enter the number of elements: "))
arr = []

# Loop to accept all elements
for _ in range(n):
    element = int(input("Enter an element: "))
    arr.append(element)

# Call selection sort and print the sorted array
sorted_arr = selectionSort(arr)
print("Sorted array:", sorted_arr)
