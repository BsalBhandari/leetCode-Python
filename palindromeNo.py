class Solution(object):
    def isPalindrome( x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        return x == x[::-1]
    
test1= Solution
print(test1.isPalindrome(x =121))
print(test1.isPalindrome(x=-121))

'''
x=121
True
x=-121
False
'''
