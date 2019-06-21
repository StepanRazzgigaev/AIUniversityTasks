def BinSearch (arr, left, right, x_pos): 
  
    # check that arguments are correct 
    if right >= left: 
  
        mid = left + (right - left)//2
  
        if arr[mid] == x: 
            return mid 
          
        # If smaller than mid, go to left array part
        elif arr[mid] > x: 
            return BinSearch(arr, left, mid-1, x) 
  
        # Else go to the right 
        else: 
            return BinSearch(arr, mid + 1, right, x) 
  
    else: 
        # Can't be found
        return -1
  
# Test Data
arr = [ 1, 2, 5, 11, 24, 35, 78, 98] 
x = 78
  
# Binary Search execution
result = BinSearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element index is % d" % result )
else: 
    print("Position not found")
