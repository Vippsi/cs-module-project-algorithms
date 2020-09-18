'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    # should probably set up an array that extends nums with the bounds of k
    # set up a loop, at each iteration use max() to get the max value, 
    # at the end of the loop append the next item in the list and pop the last, repeat! 

    count = k-1
    start = 0
    end = k

    print(f"starting count: {count}")
    arr = nums[start:end]
    results = []

    while count <= len(nums)-1:
        max_num = max(arr)
        results.append(max_num)
        print(f"results after each append {results}")
        if count == len(nums) -1:
            return results
        else:
            count += 1
            print(f"incrementing count: {count}")

            arr.append(nums[count])
            arr.pop(0)
    return results


    # arr = nums[start:end]
    # print(arr)
    # results =[]
    # while count <= len(nums) - k + 1:
    #     for x in range(0, k):
    #         # if count < len(nums) -1:
    #         print(f"[{arr}] count: {count}")


    #         max_num = max(arr)
    #         arr.append(nums[count])
    #         arr.pop(0)
    #         count +=1 
    #     # else:
    #     #     return results
    #     results.append(max_num)

            # print(results)

    # return results

    # results = []

    # for i in range(0, len(nums) - k + 1):
    #     max_values = nums[i]
    #     for j in range(0, k):
    #         if nums[i + j] > max_values:
    #             max_values = nums[i + j]
    #     results.append(max_values)
    # return results


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
