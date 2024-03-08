# import BinarySearch Class from binSearch File
# call it whatever you want
from binSearch import BinarySearch

# Assign your array with any number
arr = [2, 5, 8, 11, 15, 18, 22, 25, 28, 31]

# BinarySearch(YourArrayHere)
# BinarySearch.BinSearch(YourArrayHere , YourElementYouSearchFor )
b = BinarySearch(arr)
z = b.BinSearch(arr , 15)
print(z)
# Should print
# found at index : 4