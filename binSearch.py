import math
# --------
class BinarySearch:
    def __init__(self  , right):
        self.right = right
    def BinSearch(self, arr, searchingElement, left=0,):
        self.right = len(arr)
        while left <= self.right:
            mid = math.floor((left + self.right) / 2)
            if arr[mid] == searchingElement:
                return f"found at index : {mid}" 
            if arr[mid] > searchingElement : 
                self.right = mid - 1
            else : 
                left = mid +1

