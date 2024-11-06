from merging import Merge

def merge_sort(a=[]):
    if(len(a)==1):
        return a
    
    mid = len(a) // 2
    left = a[:mid]
    right = a[mid:]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    return Merge(sorted_left,sorted_right)

a = [8,6,9,7,96,87,25]
print("\n\nSorted array is--",merge_sort(a))