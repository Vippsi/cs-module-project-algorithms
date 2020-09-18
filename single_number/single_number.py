'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    nums = []
    for i in arr:
        if i in nums:
            nums.remove(i)
        else:
            nums.append(i)
    return nums.pop()

        

    # cool bitwise exclusive opporator solution i found
    # a = 0
    # for i in arr:
    #     a ^= i
    # return a


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")