#The more efficient quicksort
def partition(arr,low,high):
  pivot = arr[high]
  i = low - 1 #pointer to where to put lower element
  for j in range(low,high): #iterate over all elements
    if arr[j] < pivot:
      i = i + 1
      (arr[i],arr[j]) = (arr[j],arr[i])  #swapping
  (arr[i+1],arr[high]) = (arr[high],arr[i+1]) #put pivot in the middle by swapping it with the first higher element
  return i+1 #return pivot position

def quicksort(array,start,end):
  if start < end:
    c_pivot = partition(array,start,end)
    quicksort(array,start,c_pivot-1) #sort left array of pivot
    quicksort(array,c_pivot+1,end) #sort right array of pivot


#The less efficient quicksort
def partition2(arr,low,high):
  pivot = max(arr) #assign pivot = max element
  i = low - 1 #pointer to where to put lower entry
  for j in range(low,high): #iterate
    if arr[j] < pivot:
      i = i + 1
      (arr[i],arr[j]) = (arr[j],arr[i])  #swapping high with low
  (arr[i+1],arr[high]) = (arr[high],arr[i+1]) #put pivot in the middle by swapping it with the first higher element
  return i+1 #pivot position

def quicksort2(array,start,end):
  if start < end:
    c_pivot = partition2(array,start,end)
    quicksort2(array,start,c_pivot-1) #sort left of pivot
    quicksort2(array,c_pivot+1,end) #sort right of pivot


if __name__ == "__main__":
  array = input('Input test case without square bracket: ')
  arr = [int(i) for i in array.split(',')]
  quicksort(arr,0,len(arr)-1)
  print(arr)
