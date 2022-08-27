from functools import cache

def make_coins(n, denoms):
    @cache
    def backtrack(sum_rem, curr_denom_idx):
        if curr_denom_idx >= len(denoms)-1: return 1  # We can always make the sum if we reach the last index since its a 1 and we can sum any number with infinite 1s.

        denom_amount = denoms[curr_denom_idx]
        ways = 0
        
        for total_denom_amount in range(0, sum_rem+1, denom_amount):  # Note how this for loop never subtracts too much away from sum_rem
            ways += backtrack(sum_rem - total_denom_amount, curr_denom_idx+1)
        
        return ways

    return backtrack(n, 0)


if __name__ == "__main__":
    denoms = [25, 10, 5, 1]

    print(make_coins(25, denoms))