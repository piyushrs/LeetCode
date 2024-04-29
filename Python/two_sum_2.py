ans = 18
nums = [2, 7, 11, 15]

def two_sum(ans, nums):
    L = 0
    R = len(nums)-1

    while L < R:
        temp = nums[L] + nums[R]
        if temp == ans:
            return (L+1, R+1)
        elif temp < ans:
            L += 1
        elif temp > ans:
            R -= 1

if __name__ == "__main__":
    print(two_sum(ans, nums))