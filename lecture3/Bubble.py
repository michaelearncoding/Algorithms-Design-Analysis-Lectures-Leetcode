A = [-5, 3, 2, 1, 4, 0, -2, 6, 5]

def bubble_sort(arr):
    n = len(arr)
    flag = True
    while flag:
        flag = False
        for i in range(1,n):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                flag = True
    
bubble_sort(A)
print(A)  # Output should be the sorted array