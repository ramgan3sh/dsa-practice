def binary_search(lst, target):
    low = 0
    high = len(lst) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if lst[mid] == target:
            return mid  # Target found
        
        elif lst[mid] < target:
            low = mid + 1  # Search in the upper half
        
        else:
            high = mid - 1  # Search in the lower half
    
    return -1  # Target not found

lst = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Input the number to find: "))

index = binary_search(lst, target)
if index != -1:
    print(f"Element found at index {index}")
else:
    print("Element not found in the list")

