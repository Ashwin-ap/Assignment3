Question 1
Given an integer array nums of length n and an integer target, find three integers
in nums such that the sum is closest to the target.
Return the sum of the three integers.

def threeSumClosest(nums, target):
    nums.sort()  # Sort the input array
    n = len(nums)
    closestSum = float('inf')  # Initialize closestSum with a large value

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            currentSum = nums[i] + nums[left] + nums[right]

            if currentSum == target:
                return target

            if abs(currentSum - target) < abs(closestSum - target):
                closestSum = currentSum

            if currentSum > target:
                right -= 1
            else:
                left += 1

    return closestSum

Q2. Given an array nums of n integers, return an array of all the unique quadruplets
def fourSum(nums, target):
    nums.sort()  # Sort the input array
    n = len(nums)
    result = []

    for a in range(n - 3):
        if a > 0 and nums[a] == nums[a - 1]:
            continue

        for b in range(a + 1, n - 2):
            if b > a + 1 and nums[b] == nums[b - 1]:
                continue

            c = b + 1
            d = n - 1

            while c < d:
                currentSum = nums[a] + nums[b] + nums[c] + nums[d]

                if currentSum == target:
                    result.append([nums[a], nums[b], nums[c], nums[d]])
                    c += 1
                    d -= 1

                    while c < d and nums[c] == nums[c - 1]:
                        c += 1
                    while c < d and nums[d] == nums[d + 1]:
                        d -= 1

                elif currentSum < target:
                    c += 1
                else:
                    d -= 1

    return result

Q3. A permutation of an array of integers is an arrangement of its members into a
sequence or linear order.
def nextPermutation(nums):
    n = len(nums)
    i = n - 2

    # Find the first pair nums[i] and nums[i-1] where nums[i] > nums[i-1]
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        # Find the smallest element greater than nums[i-1] to swap with
        j = n - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1

        # Swap nums[i-1] with nums[j]
        nums[i], nums[j] = nums[j], nums[i]

    # Reverse the subarray nums[i:]
    left = i + 1
    right = n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums

Q4. Given a sorted array of distinct integers and a target value, return the index if the
target is found. If not, return the index where it would be if it were inserted in
order.
def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

Q5. You are given a large integer represented as an integer array digits, where each
digits[i] is the ith digit of the integer. The digits are ordered from most significant
to least significant in left-to-right order. The large integer does not contain any
leading 0's.
def plusOne(digits):
    carry = 1

    for i in range(len(digits) - 1, -1, -1):
        digits[i] += carry

        if digits[i] <= 9:
            carry = 0
            break
        else:
            digits[i] = 0

    if carry == 1:
        digits.insert(0, 1)

    return digits

Q6. Given a non-empty array of integers nums, every element appears twice except
for one. Find that single one.

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

Q7. You are given an inclusive range [lower, upper] and a sorted unique integer array
nums, where all elements are within the inclusive range.

def findMissingRanges(nums, lower, upper):
    result = []
    n = len(nums)

    if lower < nums[0]:
        result.append(getRange(lower, nums[0] - 1))

    for i in range(1, n):
        if nums[i] > nums[i-1] + 1:
            result.append(getRange(nums[i-1] + 1, nums[i] - 1))

    if upper > nums[-1]:
        result.append(getRange(nums[-1] + 1, upper))

    return result


def getRange(start, end):
    if start == end:
        return str(start)
    else:
        return str(start) + "->" + str(end)

Q8. Given an array of meeting time intervals where intervals[i] = [starti, endi],
determine if a person could attend all meetings.

def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort intervals based on start time

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False

    return True
