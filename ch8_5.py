import time
from functools import cache



#  # Approach 1
# def min_product(a, b):
#     def min_product_helper(a, b):
#         if b == 1: return a
#         return a + min_product_helper(a, b-1)
#     return min_product_helper(max(a, b), min(a, b))

# # Approach 2
# def min_product(a, b):
#     def min_product_helper(a, b):
#         if b == 0: return 0
#         if b == 1: return a
#         b_half = b >> 1
#         if b % 2 == 0:  # Even case: return the number doubled
#             return min_product_helper(a, b_half) << 1
#         else:  # Odd case: Try to split as close to half as possible (with one side even, one odd) and recurse on that
#             return min_product_helper(a, b_half) + min_product_helper(a, b - b_half)
#     return min_product_helper(max(a, b), min(a, b))
 

# # Approach 3
# def min_product_memo(a, b):
#     @cache
#     def min_product_helper(a, b):
#         if b == 0: return 0
#         if b == 1: return a
#         b_half = b >> 1
#         if b % 2 == 0:  # Even case: return the number doubled
#             return min_product_helper(a, b_half) << 1
#         else:  # Odd case: Try to split as close to half as possible (with one side even, one odd) and recurse on that
#             return min_product_helper(a, b_half) + min_product_helper(a, b - b_half)
#     return min_product_helper(max(a, b), min(a, b))

# Approach 4
def min_product(a, b):
    def min_product_helper(a, b):
        if b == 0: return 0
        if b == 1: return a
        b_half = b >> 1
        res = min_product_helper(a, b_half) << 1
        if b % 2 == 1: res += a
        return res
    return min_product_helper(max(a, b), min(a, b))

if __name__ == '__main__':
    print("3 * 2 = " ,min_product(3,2))
    print("3 * 4 = ",min_product(4, 3))
    print("8 * 7 = ",min_product(7, 8))
    print("9 * 9 = ",min_product(9,9))

    # tic = time.perf_counter()
    # print("34563251314512 * 8417341124141241 = ",min_product(34563251314512,8417341124141241))
    # toc = time.perf_counter()
    # print(f"Took {toc - tic:0.4f} seconds to run the big multiplication without memo")

    # tic = time.perf_counter()
    # print("34563251314512 * 8417341124141241 = ", min_product_memo(34563251314512,8417341124141241))
    # toc = time.perf_counter()
    # print(f"Took {toc - tic:0.4f} seconds to run the big multiplication with memo")

