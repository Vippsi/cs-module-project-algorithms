'''
Input: a List of integers
Returns: a List of integers
'''
# def moving_zeroes(arr):
#     # Your code here
#     left =[]
#     right = []

#     # O(n)
#     for x in arr:
#         if x == 0:
#             right.append(x)
#         else:
#             left.append(x)
   
#     arr = left + right
#     # print(arr)
#     return arr
  
            
def moving_zeroes(arr):
    left = 0
    right = len(arr) -1

    while left< right:
        if arr[left] == 0:
            if arr[right] != 0:
                arr[left], arr[right] = arr[right], arr[left]
                right -= 1
                left += 1
            else:
                right -= 1
        else:
            left += 1
    return arr

        



    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 2, 3, 0, 4, 0, 0,]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")