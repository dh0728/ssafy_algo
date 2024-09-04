import sys
sys.stdin = open('input.txt')

def merge(left,right):
    result = [0] * (len(left)+len(right))
    l = r = 0

def merge_sort(num_list):
    if len(num_list) == 1:
        return

    middle= len(num_list)//2
    left = num_list[:middle]
    right = num_list[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left,right)