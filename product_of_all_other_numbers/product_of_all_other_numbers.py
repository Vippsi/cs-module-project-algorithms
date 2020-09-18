'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here
    # when iterating over the input array 
    # the expected value at the current iteration index
    # needs to be the product of every number except at the 
    # current iteration index 

    # what if the array is too small to do multiplication: [1,4]

    # need to iterate through the list, maybe need the value and the index, use enumerate
    # needs to check what index we're at, exclude that value form our math
   




    result = 1
    for i, value in enumerate(arr):
        result *= value
        
    for j, value2 in enumerate(arr):
        arr[j] = result// value2

    return arr

    # to achieve O(n) time, need 1 loop

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [3, 2]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
