# You are going to be given an array of integers. Your job is to take that
# array and find an index N where the sum of the integers to the left of N
# is equal to the sum of the integers to the right of N. If there is no index
# that would make this happen, return -1.
#
# For example:
#
# Let's say you are given the array {1,2,3,4,3,2,1}:
# Your function will return the index 3, because at the 3rd position of the array,
# the sum of left side of the index ({1,2,3}) and the sum of the right side of the
# index ({3,2,1}) both equal 6.

def find_even_index(arr):
    N_exist = False
    for N in range(len(arr)):
        if sum(arr[0: N: 1]) == sum(arr[len(arr): N: -1]):
            # note: review array slicing arr[start:end:step]
            N_exist = True
            break
    if N_exist == True:
        return N
    else:
        return -1

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 3, 2, 1]
    print(find_even_index(arr))
