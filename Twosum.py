class Twosum(object):

    # def __init__(self, nums , target):
    #     self.nums = nums
    #     self.target =target

    def twoSum(self, nums, target):
        hashMap= {} # index , value
        for i, n in enumerate(nums): # enumerate helps us get index and num, in this case i is index and n is number
            diff = target - n
            if diff in hashMap:
                return[i,hashMap[diff]] 
            hashMap[n] = i

testcase_1 = Twosum()
testcase_1.twoSum([2,5,11,15,7], 9)

'''
Input -> nums = [2,5,11,15,7] , target = 9
Output = 0,4
'''