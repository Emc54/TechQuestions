"""
Quick Sort

// Sorts a (portion of an) array, divides it into partitions, then sorts those
algorithm quicksort(A, lo, hi) is 
  // Ensure indices are in correct order
  if lo >= hi || lo < 0 then 
    return
    
  // Partition array and get the pivot index
  p := partition(A, lo, hi) 
      
  // Sort the two partitions
  quicksort(A, lo, p - 1) // Left side of pivot
  quicksort(A, p + 1, hi) // Right side of pivot

// Divides array into two partitions
algorithm partition(A, lo, hi) is 
  pivot := A[hi] // Choose the last element as the pivot

  // Temporary pivot index
  i := lo

  for j := lo to hi - 1 do 
    // If the current element is less than or equal to the pivot
    if A[j] <= pivot then 
      // Swap the current element with the element at the temporary pivot index
      swap A[i] with A[j]
      // Move the temporary pivot index forward
      i := i + 1

  // Swap the pivot with the last element
  swap A[i] with A[hi]
  return i // the pivot index
"""

def quicksort(l, low, high):
    if low >= high or low < 0:
        return
    
    pivot = partition(l, low, high)

    quicksort(l, low, pivot-1)
    quicksort(l, pivot+1, high)

def partition(l, low, high):
    pivot = l[high]

    i = low

    for j in range(low,high):
        if l[j] <= pivot:
            (l[i],l[j]) = (l[j],l[i])
            i += 1

    (l[i],l[high]) = (l[high],l[i]) 
    return i


example_list = [2,4,32,54,2,4,2,1,3,5,56,8,3]

quicksort(example_list,0,len(example_list)-1)
print(example_list)
