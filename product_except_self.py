
'''
Problem statement:
    Given an integer array nums, return an array answer such that answer[i] is equal to
    the product of all the elements of nums except nums[i].
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
    You must write an algorithm that runs in O(n) time and without using the division operation.


Solution statement:
    To solve this problem efficiently in O(n) time without using division,
    we can use a two-pass approach where we calculate the product of all elements
    to the left of each element and the product of all elements to the right of each element.
    We then combine these two products to get the desired result.
'''


def product_except_self(nums):
    length = len(nums)
    left_answer = [1] * length
    right_answer = [1] * length

    # First pass from left to right
    left_product = 1
    for i in range(length):
        left_answer[i] = left_product
        left_product *= nums[i]

    # Second pass from right to left
    right_product = 1
    for j in range(length-1, -1, -1):
        right_answer[j] = right_product
        right_product *= nums[j]

    # Zipping both lists using list comprehension
    return ([x*y for x, y in zip(left_answer, right_answer)])


print(product_except_self([1, 2, 3, 4]))
