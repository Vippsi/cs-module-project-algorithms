'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    left =[]
    right = []

    for x in arr:
        if x == 0:
            right.append(x)
        else:
            left.append(x)

    print(f"This is the left list {left}")    
    print(f"This is the right list {right}")    
    print(left.extend(right))
    # print(arr)
    return arr


    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")